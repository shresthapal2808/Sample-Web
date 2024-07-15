import json
import requests
from .models import Contact
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname', 'Chuck')
        lastname = request.POST.get('lname', 'Norris')
        full_name = f"{firstname} {lastname}"

        try:
            r = requests.get('https://api.chucknorris.io/jokes/random')
            r.raise_for_status()  # Raise an error for bad status codes
            json_data = r.json()
            joke = json_data.get('value', 'No joke found.')
            joke = joke.replace('Chuck Norris', full_name)  # Replace "Chuck Norris" with the custom name
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            joke = 'Error fetching joke.'

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)

        # GET request handling (default joke)
    return render(request, 'mysite/index.html', {})



def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')
