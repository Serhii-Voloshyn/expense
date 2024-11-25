# External imports
from django.urls import path

# Internal imports
from .views import ExpenseViewSet

# Viewset actions
expense_list = ExpenseViewSet.as_view({'get': 'list', 'post': 'create'})
expense_detail = ExpenseViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})
expense_by_date_range = ExpenseViewSet.as_view({'get': 'by_date_range'})
expense_category_summary = ExpenseViewSet.as_view({'get': 'category_summary'})

# URL patterns
urlpatterns = [
    path('expenses/', expense_list, name='expense-list'),
    path('expenses/<int:pk>/', expense_detail, name='expense-detail'),
    path('expenses/date-range/<int:user_id>/', expense_by_date_range, name='expenses-date-range'),
    path('expenses/summary/<int:user_id>/<int:month>/', expense_category_summary, name='category-summary'),
]