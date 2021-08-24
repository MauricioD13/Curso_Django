from django.http import HttpResponse
import json
# Utilities
from datetime import datetime

def hello_world(request):
    """[summary]

    Args:
        request (class): Http resquest object

    Returns:
        Http response 
    """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    
    return HttpResponse(f'<h1>Hello, world</h1> <p>Current server time is</p> {now}')

def sort_numbers(request):
    """ It sort a list of numbers that came from the URL
    Args:
        request (class): Http resquest object
    Returns:
        Http response: With JSON str and numbers sorted
    """
    #Debugger python 
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers_sorted = [int(i) for i in numbers]
    numbers_sorted.sort()
    jsonStr = json.dumps(numbers_sorted)
    data = {
        'status' : 'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
    #return HttpResponse(f"Hi <p>{jsonStr}</p>")

def hi(request, name, age): 
    """If the path have more arguments then those
    arguments most be in the function parameters
    """
    if age<12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello, {name}! Welcome to Platzigram'
    return HttpResponse(message)