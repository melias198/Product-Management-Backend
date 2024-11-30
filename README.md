# Product Management Backend

## 1. Overview
**Project Name**: Zero Shop

**Description**:
Zero Shop is a full-stack application with CRUD functionality, allowing admins to add, update, and delete products. Authenticated and unauthenticated users can view products, see product details, search, and navigate through paginated results. The application also supports user registration and login features.


## 2. Backend
- **Django**: Serves as the backend framework to manage server-side logic and database operations.
- **Django REST Framework (DRF)**: Enables building RESTful APIs that allow frontend and backend communication.
- **Django JWT Authentication**: Secures the application using JSON Web Tokens for user authentication.

## 3. Database
- **SQLite**: Utilizes SQLite as the database for simplicity and ease of setup.

## 4. Deployment
- **Render**: Deploys the backend Django API, ensuring a scalable and reliable backend service.
- **Live Link**: [Backend Live Link](https://zeroshop.onrender.com/)
- **API Documentation**: [Swagger UI](https://zeroshop.onrender.com/api/doc/)



## 5. Installation and Setup
* Clone Repository
 ```
git clone 
```
* Database Setup
```
python manage.py migrate
```
* Run Server
```
python manage.py runserver
```

    

## 6. API Endpoints

| Endpoint                  | Method | Description                            | Authentication |
|---------------------------|--------|----------------------------------------|----------------|
| **User Registration**     | POST   | Register a new user                   | No             |
| `/user/register/`         |        |                                        |                |
| **User Login**            | POST   | Log in an existing user               | No             |
| `/user/api/token/`            |        |                                        |                |
| **Product List**          | GET    | Retrieve a list of all products       | No            |
| `/api/products/`          |        |                                        |                |
| **Product Search**        | GET    | Search for products by keyword        | No            |
| `/api/products/?search=<query>` |  | Add `search=<query>` as query param   |                |
| **Product Pagination**    | GET    | Retrieve products with pagination     | No            |
| `/api/products/?page=<page_number>` | | Add `page` query params | |
| **Product Detail**        | GET    | Get details of a specific product     | No            |
| `/api/products/<id>/`     |        |                                        |                |
| **Create Product**        | POST   | Create a new product                  | Yes            |
| `/api/products/`          |        |                                        |                |
| **Update Product**        | PUT    | Update an existing product            | Yes            |
| `/api/products/<id>/`     |        |                                        |                |
| **Delete Product**        | DELETE | Delete a specific product             | Yes            |
| `/api/products/<id>/`     |        |                                        |                |
| **Logout**                | POST   | Log out user and blacklist token      | No            |
| `/user/logout/`       |        |                                        |                |

## 7. Example API Details

Each endpoint is expanded with specific details like request/response format, required parameters, and sample payloads.

### User Registration

- **Endpoint**: `/user/register/`
- **Method**: `POST`
- **Description**: Registers a new user.

**Request Example**:

```json
{
  "username": "dummyuser",
  "email": "dummy@example.com",
  "first_name": "Mr",
  "last_name": "Dummy",
  "password": "1234"
}
```
### Product List
- **Endpoint**: `/api/products/`
- **Method**: `GET`
- **Description**: Retrieves a list of all products.

**Response Example**:
```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 6,
    "next": "http://zeroshop.onrender.com/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Mobile",
            "description": "Samsung Mobile",
            "price": "10000.00",
            "quantity": 6
        },
        {
            "id": 2,
            "name": "Watch G2",
            "description": "G2 Watch Made By China",
            "price": "1890.00",
            "quantity": 10
        },
        {
            "id": 3,
            "name": "Logitech Headphone H105",
            "description": "This is the best headphone for daily use.",
            "price": "980.00",
            "quantity": 4
        }
    ]
}
```