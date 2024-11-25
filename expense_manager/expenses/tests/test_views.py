import pytest
from rest_framework.test import APIClient
from .factories import UserFactory, ExpenseFactory


@pytest.mark.django_db
def test_get_expenses_list():
    user = UserFactory()
    ExpenseFactory.create_batch(5, user=user)

    client = APIClient()
    response = client.get("/expenses/")
    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_create_expense():
    user = UserFactory()
    client = APIClient()
    data = {
        "user": user.id,
        "title": "Dinner",
        "amount": 25.50,
        "date": "2024-11-21",
        "category": "Food",
    }
    response = client.post("/expenses/", data)
    assert response.status_code == 201
    assert response.data["title"] == "Dinner"


@pytest.mark.django_db
def test_get_expenses_by_date_range():
    user = UserFactory()
    ExpenseFactory(user=user, date="2024-11-01")
    ExpenseFactory(user=user, date="2024-11-15")
    ExpenseFactory(user=user, date="2024-12-01")

    client = APIClient()
    response = client.get(
        f"/expenses/date-range/{user.id}/?start=2024-11-01&end=2024-11-30")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_category_summary():
    user = UserFactory()
    ExpenseFactory(user=user, category="Food", amount=10)
    ExpenseFactory(user=user, category="Food", amount=20)
    ExpenseFactory(user=user, category="Travel", amount=30)

    client = APIClient()
    response = client.get(f"/expenses/summary/{user.id}/11/")
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["category"] == "Food"
    assert response.data[0]["total"] == 30
