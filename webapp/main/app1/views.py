from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

import requests


def home(request):
    assert isinstance(request, HttpRequest)
    r = requests.get('http://127.0.0.1:5000/query==It%was%a%good%movie')

    jj = r.json()

    print(r.status_code)

    return render(
        request,
        'app1/index.html',
        {
            'title': "Home Page",
            'year':datetime.now().year,
        }
    )