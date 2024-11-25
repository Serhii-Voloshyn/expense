import factory
from datetime import date
from expenses.models import User, Expense

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")

class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("word")
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    date = factory.LazyFunction(date.today)
    category = factory.Faker("random_element", elements=[choice[0] for choice in Expense.CATEGORY_CHOICES])