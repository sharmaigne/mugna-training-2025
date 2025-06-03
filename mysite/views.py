from django.http import HttpResponse, Http404
import datetime
from math import prod
from functools import reduce

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World!")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, "current_datetime.html", {"current_datetime": now})

def datetime_offset(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404("Invalid offset value")
    
    offset_time = datetime.datetime.now() + datetime.timedelta(hours=offset)

    return render(request, "datetime_offset.html", {"offset": offset, "offset_time": offset_time})


# accepts 2 or 3 integers as parameters and displays their sum, product, difference, and quotient.
def calculate(request, numbers):

    try:
        numbers = [int(num) for num in numbers.split("/")]
        if len(numbers) not in (2, 3):
            raise ValueError("Must provide 2 or 3 integers")

    except ValueError:
        raise Http404("Invalid parameter value")

    total_sum = sum(numbers)
    product = prod(numbers)

    difference = (
        2 * numbers[0]
    ) - total_sum  # equivalent to numbers[0] - (total_sum - numbers[0])

    # zero check
    if 0 in numbers[1:]:
        raise Http404("Cannot divide by zero")

    quotient = reduce(lambda x, y: x / y, numbers) if len(numbers) > 1 else numbers[0]

    return render(
        request,
        "calculate.html",
        {
            "numbers": numbers,
            "sum": total_sum,
            "product": product,
            "difference": difference,
            "quotient": quotient,
        },
    )


# accept date and distinguish if valid or not
def is_valid_date(request, year, month, day):
    try:
        year, month, day = [int(x) for x in (year, month, day)]

    except ValueError:
        raise Http404("Should be positive integers")

    try:
        datetime.datetime(year, month, day)
        is_valid = True
    except ValueError:
        is_valid = False

    return render(
        request,
        "valid_date.html",
        {
            "year": year,
            "month": month,
            "day": day,
            "is_valid": is_valid,
        },
    )
