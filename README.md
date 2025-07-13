# Product Review System API

Django REST API for managing products and reviews.

## How to Run

```
pip install -r requirements.txt
python manage.py runserver
```

## Admin Credentials

- Username: admin
- Password: admin

Use these to:
- Log in at `/api/login/`
- Add, edit, or delete products

## Main API Endpoints

- POST `/api/register/` - Register user
- POST `/api/login/` - Get JWT token
- GET `/api/products/` - List products
- POST `/api/products/` - Add product (admin only)
- PUT/DELETE `/api/products/{id}/` - Edit/Delete product (admin only)
- POST `/api/products/{id}/reviews/` - Add review (logged-in user)
- GET `/api/products/{id}/reviews/list/` - View reviews

## Auth Header

```
Authorization: Bearer <access_token>
```
