from django.shortcuts import render

# Create your views here.


def home(respone):
    return render(respone,"base.html",{})