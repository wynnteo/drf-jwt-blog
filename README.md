# JWT Authentication in Django REST Framework with SimpleJWT

A **Django REST Framework** project demonstrating **JWT Authentication** with **SimpleJWT**, including refresh rotation, blacklisting (logout), owner/admin permissions, and a small Blog app. For a detailed tutorial, you may [visit](https://cloudfullstack.dev/jwt-authentication-in-django-rest-framework/).

## Features
- JWT auth with access + refresh tokens
- Refresh token rotation + blacklisting (logout)
- Blog API with `Post` model
- Permissions: public list, authenticated create, owner-or-admin update/delete
- Protected demo endpoint (`/api/protected/`)
- Unit tests for auth flow
- SQLite by default

## Quickstart

```bash
# 1) Create and activate a virtualenv (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run migrations
python manage.py migrate

# 4) Create a superuser for login
python manage.py createsuperuser

# 5) Run the server
python manage.py runserver
```

### Endpoints

- `POST /api/token/` — login, returns access + refresh
- `POST /api/token/refresh/` — rotate refresh, returns new access (and new refresh if enabled)
- `POST /api/logout/` — blacklist the given refresh token (requires auth)
- `GET  /api/protected/` — demo protected endpoint
- `GET  /api/posts/` — public list posts
- `POST /api/posts/` — create (auth required)
- `GET/PUT/DELETE /api/posts/<id>/` — retrieve/update/delete (owner or admin)

### Example (cURL)

```bash
# Login
curl -X POST http://127.0.0.1:8000/api/token/   -H "Content-Type: application/json"   -d '{"username":"<youruser>","password":"<yourpass>"}'

# Access protected
curl http://127.0.0.1:8000/api/protected/   -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### Run tests
```bash
python manage.py test
```

## Settings Highlights
- `REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES = JWTAuthentication`
- `SIMPLE_JWT`: access = 30 min, refresh = 7 days, rotation + blacklist enabled

> For production: use HTTPS, store refresh tokens in **HttpOnly** cookies, and keep secrets out of source control.
