import pytest
from expenses.models import User, Expense

@pytest.mark.django_db
def test_user_str():
    user = User.objects.create(username="testuser", email="test@example.com")
    assert str(user) == "testuser"

@pytest.mark.django_db
def test_expense_str():
    user = User.objects.create(username="testuser", email="test@example.com")
    expense = Expense.objects.create(
        user=user, title="Lunch", amount=15.50, date="2024-11-21", category="Food"
    )
    assert str(expense) == "Lunch - 15.5"