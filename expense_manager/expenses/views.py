# External imports
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum

# Internal imports
from .models import Expense
from .serializers import ExpenseSerializer
from .utils import validate_month, validate_date_range


class ExpenseViewSet(viewsets.ViewSet):
    # Standard CRUD operations
    def list(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found."},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            expense = Expense.objects.get(pk=pk)
            expense.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found."},
                            status=status.HTTP_404_NOT_FOUND)

    # Custom actions
    @action(detail=False, methods=['get'],
            url_path='by-date-range/(?P<user_id>[^/.]+)')
    def by_date_range(self, request, user_id=None):
        start_date = request.query_params.get('start')
        end_date = request.query_params.get('end')
        try:
            start_date, end_date = validate_date_range(start_date, end_date)
        except ValidationError as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

        expenses = Expense.objects.filter(user_id=user_id,
                                          date__range=[start_date, end_date])
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'],
            url_path='category-summary/(?P<user_id>[^/.]+)/(?P<month>[^/.]+)')
    def category_summary(self, request, user_id=None, month=None):
        try:
            month = validate_month(month)
        except ValidationError as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

        expenses = Expense.objects.filter(user_id=user_id, date__month=month)
        if not expenses.exists():
            return Response([], status=status.HTTP_200_OK)

        summary = expenses.values('category').annotate(total=Sum('amount'))
        return Response(summary, status=status.HTTP_200_OK)
