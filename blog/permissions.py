from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        author = getattr(obj, "author", None)
        return author == request.user

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner | IsAdminUser]   # Owner OR admin