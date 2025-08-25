# 📘 API Endpoints: Book Management

This project implements CRUD operations for the `Book` model using Django REST Framework's **generic views**.  
Permissions are applied to ensure public read-only access and authenticated write access.

---

## Endpoints

### 1. List All Books
- **URL:** `/api/books/`
- **Method:** `GET`
- **Access:** Public
- **Features:**
  - Search books by title or author name: `?search=potter`
  - Order results: `?ordering=title` or `?ordering=-publication_year`

### 2. Retrieve a Single Book
- **URL:** `/api/books/<pk>/`
- **Method:** `GET`
- **Access:** Public

### 3. Create a New Book
- **URL:** `/api/books/create/`
- **Method:** `POST`
- **Access:** Authenticated users only
- **Body Example:**
  ```json
  {
    "title": "The Hobbit",
    "publication_year": 1937,
    "author": 1
  }
