from django.shortcuts import render
import requests
from .models import *

# Create your views here.

def index(request):
    #Live Gold rate
    url1 = "https://gold-silver-live-prices.p.rapidapi.com/getGoldRate"

    querystring1 = {"place": "kalyan"}

    headers1 = {
        "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
        "x-rapidapi-host": "gold-silver-live-prices.p.rapidapi.com"
    }
    #Live Silver Rate
    url2 = "https://gold-silver-live-prices.p.rapidapi.com/getSilverRate"

    querystring2 = {"place": "chennai"}

    headers2 = {
        "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
        "x-rapidapi-host": "gold-silver-live-prices.p.rapidapi.com"
    }
    #Gold history
    querystring3 = {"place": "hyderabad", "no_of_days": "100"}

    headers3 = {
        "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
        "x-rapidapi-host": "gold-silver-live-prices.p.rapidapi.com"
    }
    response3 = requests.get("https://gold-silver-live-prices.p.rapidapi.com/getGoldPriceHistory", headers=headers3,
                            params=querystring3)

    response1 = requests.get(url1, headers=headers1, params=querystring1)
    response2 = requests.get(url2, headers=headers2, params=querystring2)

    apidata1 = response1.json()
    apidata2 = response2.json()
    apidata3 = response3.json()

    context = {
        "gold": apidata1,
        "silver": apidata2,
        "data1": apidata3,
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "pages-contact.html")


def login(request):
    return render(request, "pages-login.html")

def savelogin(request):
    return render(request, "pages-login.html")


def register(request):

    return render(request, "pages-register.html")

def saveregister(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        user = signup(name=name, email=email, username=username, password=password)
        user.save()
        print("Account Created")
    else:
        print('Error ocurred')
    return render(request, "pages-login.html")


def gold(request):

    querystring = {"place": "hyderabad", "no_of_days": "100"}

    headers = {
        "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
        "x-rapidapi-host": "gold-silver-live-prices.p.rapidapi.com"
    }
    response = requests.get("https://gold-silver-live-prices.p.rapidapi.com/getGoldPriceHistory", headers=headers,
                            params=querystring)

    apidata = response.json()

    context = {
        "data" : apidata
    }
    return render(request, "tables-gold.html", context)

def silver(request):
    url = "https://gold-silver-live-prices.p.rapidapi.com/getSilverPriceHistory"

    querystring = {"place": "lucknow", "no_of_days": "365"}

    headers = {
        "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
        "x-rapidapi-host": "gold-silver-live-prices.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    apidata = response.json()

    context = {
        "data" : apidata
    }
    return render(request, "tables-silver.html", context)
