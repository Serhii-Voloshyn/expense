# External imports
from datetime import datetime
from rest_framework.exceptions import ValidationError


# Validation utilities
def validate_month(month):
    try:
        month = int(month)
        if 1 <= month <= 12:
            return month
        else:
            raise ValueError("Month must be between 1 and 12.")
    except ValueError:
        raise ValidationError("Month must be an integer between 1 and 12.")


def validate_date_range(start_date, end_date):
    if not start_date or not end_date:
        raise ValidationError("Both start and end dates are required.")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        return start_date, end_date
    except ValueError:
        raise ValidationError("Invalid date format. Use YYYY-MM-DD.")