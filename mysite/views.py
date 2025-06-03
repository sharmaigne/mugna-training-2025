from django.http import HttpResponse, Http404
import datetime
from math import prod
from functools import reduce


def index(request):
    return HttpResponse("Hello World!")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def current_datetime_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404("Invalid offset value")
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, now)
    return HttpResponse(html)


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

    difference = (2*numbers[0]) - total_sum # equivalent to numbers[0] - (total_sum - numbers[0])
    
    # zero check
    if 0 in numbers[1:]:
        raise Http404("Cannot divide by zero")
    
    quotient = reduce(lambda x, y: x / y, numbers) if len(numbers) > 1 else numbers[0]

    html = (
        "<html><body>Sum: %s, Product: %s, Difference: %s, Quotient: %s</body></html>"
        % (total_sum, product, difference, quotient)
    )
    return HttpResponse(html)


# accept date and distinguish if valid or not
def is_valid_date(request, year, month, day):
    try:
        year, month, day = [int(x) for x in (year, month, day)]

    except ValueError:
        raise Http404("Should be positive integers")
    
    is_valid = False
    try:
        newDate = datetime.datetime(year, month, day)
        is_valid = True
    except ValueError: 
        pass

    html = (
        "<html><body>Date: %s-%s-%s is %s.</body></html>"
        % (year, month, day, "valid" if is_valid else "invalid")
    )

    return HttpResponse(html)