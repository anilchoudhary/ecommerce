from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {
        "title": "Hello, I am Anil Choudhary.",
        "content": "Welcome to the Homepage."
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About page",
        "content": "Welcome to the about page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        "title": "Contact page",
        "content": "Welcome to the contact page"
    }
    if request.method == "POST":
        # print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def shop_page(request):
    context = {
    "title": "Shop page",
    "content": "Welcome to the shop page"
    }
    return render(request, "home_page.html", context)