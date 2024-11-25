import pytest
from expenses.models import User, Expense
from expenses.serializers import UserSerializer, ExpenseSerializer

@pytest.mark.django_db
def test_user_serializer():
    user = User.objects.create(username="testuser", email="test@example.com")
    serializer = UserSerializer(user)
    expected_data = {"id": user.id, "username": "testuser", "email": "test@example.com"}
    assert serializer.data == expected_data

@pytest.mark.django_db
def test_expense_serializer_validation():
    user = User.objects.create(username="testuser", email="test@example.com")
    data = {
        "user": user.id,
        "title": "Lunch",
        "amount": -10,
        "date": "2024-11-21",
        "category": "Food",
    }
    serializer = ExpenseSerializer(data=data)
    assert not serializer.is_valid()
    assert "amount" in serializer.errors