from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {
        "title": "hello i am anil",
        "content": "welcome to the home page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "about_page",
        "content": "welcome to the about page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        "title": "contact_page",
        "content": "welcome to the contact page"
    }
    return render(request, "home_page.html", context)