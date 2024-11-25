
# Expense Manager API

This project provides a simple Django REST API to help users manage their expenses. The application supports full CRUD operations for expenses, filtering by date ranges, and generating expense summaries by category.

## Features

1. **Expense Management**: Create, view, update, and delete expenses.
2. **Filter by Date Range**: Query expenses within a specific date range.
3. **Category Summaries**: Generate monthly summaries of expenses grouped by categories.

## Requirements

- Python 3.x
- Django 5.x
- Django REST Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/1gorb1lyk/expense-manager.git
   cd expense-manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Documentation

### 1. Retrieve All Expenses
**Method**: `GET`  
**Endpoint**: `/api/expenses/`  
**Response**:
```json
[
    {
        "id": 1,
        "user": 1,
        "title": "Rent",
        "amount": "800.00",
        "date": "2024-11-01",
        "category": "Housing"
    }
]
```

### 2. Add a New Expense
**Method**: `POST`  
**Endpoint**: `/api/expenses/`  
**Request Body**:
```json
{
    "user": 1,
    "title": "Electricity Bill",
    "amount": 100.50,
    "date": "2024-11-20",
    "category": "Utilities"
}
```
**Response**:
```json
{
    "id": 2,
    "user": 1,
    "title": "Electricity Bill",
    "amount": "100.50",
    "date": "2024-11-20",
    "category": "Utilities"
}
```

### 3. Retrieve a Specific Expense
**Method**: `GET`  
**Endpoint**: `/api/expenses/<id>/`  
**Response**:
```json
{
    "id": 1,
    "user": 1,
    "title": "Rent",
    "amount": "800.00",
    "date": "2024-11-01",
    "category": "Housing"
}
```

### 4. Delete an Expense
**Method**: `DELETE`  
**Endpoint**: `/api/expenses/<id>/`  
**Response**: 204 No Content

### 5. Filter Expenses by Date Range
**Method**: `GET`  
**Endpoint**: `/api/expenses/date-range/<user_id>/?start=YYYY-MM-DD&end=YYYY-MM-DD`  
**Example**:
```
/api/expenses/date-range/1/?start=2024-11-01&end=2024-11-30
```
**Response**:
```json
[
    {
        "id": 3,
        "user": 1,
        "title": "Grocery",
        "amount": "150.00",
        "date": "2024-11-12",
        "category": "Food"
    }
]
```

### 6. Monthly Expense Category Summary
**Method**: `GET`  
**Endpoint**: `/api/expenses/summary/<user_id>/<month>/`  
**Example**:
```
/api/expenses/summary/1/11/
```
**Response**:
```json
[
    {
        "category": "Food",
        "total": "150.00"
    },
    {
        "category": "Housing",
        "total": "800.00"
    }
]
```

## Additional Notes

- Ensure that `Python 3.x` and the required dependencies are installed before starting the application.
- Customize the project as needed for your use case.
- For additional help, refer to Django's official documentation.

---

Happy coding!
