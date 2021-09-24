from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.template.loader import render_to_string
import requests
import random
from .forms import CapitalGuess

r = requests.get('https://countriesnow.space/api/v0.1/countries/capital')

response = r.json()

rand_dict = response['data']

country_capital = {}

for d in rand_dict:
    country = d['name']
    capital = d['capital']
    country_capital.update({country: capital})

rand_country = random.choice(list(country_capital.keys()))

success = False

@csrf_exempt
def home(request):
    global country_capital, rand_country, success

    context = {}

    wrong = ''

    capital_guess = request.POST.get('guess_capital')

    if capital_guess == country_capital[rand_country]:
        success = True
    else:
        success = False

    context['country'] = rand_country
    context['capital'] = country_capital[rand_country]
    context['success'] = success
    context['wrong'] = wrong
    context['capital_guess'] = capital_guess

    return render(request, 'countries/home.html', {'context': context})


def about(request):
    return render(request, 'countries/about.html', {'title': 'About'})
