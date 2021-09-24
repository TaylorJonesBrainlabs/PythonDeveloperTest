import requests
import random

url = requests.get('https://restcountries.eu/rest/v2/all')

response = url.json()

country_capital = {}


for d in response:
    country = d['name']
    capital = d['capital']

    country_capital.update({country: capital})

breakpoint()

print(country_capital)
print(response)

rand_country = random.choice(list(country_capital.keys()))

print(rand_country)

print(country_capital[rand_country])

guess = input('What is the Capital: ')

while True:
    guess = input("Capital?: ")
    if guess != country_capital[rand_country]:
        print("try again")
        continue
    else:
        print("You're a Winner!")
        break
