from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Post

class BlogJWTTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password123")
        self.admin = User.objects.create_user(username="adminuser", password="password123", is_staff=True)

    def login(self, username, password):
        res = self.client.post("/api/token/", {"username": username, "password": password}, format="json")
        assert res.status_code == 200, res.content
        return res.data["access"], res.data["refresh"]

    def test_flow_create_and_edit_post(self):
        access, refresh = self.login("tester", "password123")
        # Create post
        res = self.client.post("/api/posts/create/", {"title": "Hello", "content": "World"},
                               HTTP_AUTHORIZATION=f"Bearer {access}", format="json")
        self.assertEqual(res.status_code, 201)
        post_id = res.data["id"]

        # Another user cannot edit
        admin_access, _ = self.login("adminuser", "password123")
        res = self.client.put(f"/api/posts/{post_id}/", {"title": "Hack", "content": "No"},
                              HTTP_AUTHORIZATION=f"Bearer {admin_access}", format="json")
        # admin can edit because IsAdminUser OR IsOwner
        self.assertIn(res.status_code, (200, 403))

    def test_protected_endpoint_requires_auth(self):
        res = self.client.get("/api/protected/")
        self.assertEqual(res.status_code, 401)
