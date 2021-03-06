from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Hello, I am Anil Choudhary.",
        "content": "Welcome to the Homepage.",
    }
    if request.user.is_authenticated:
        context['premium_content'] = "you are awesome"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About page",
        "content": "Welcome to the about page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in?")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Please, register with us")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


def shop_page(request):
    context = {
        "title": "Shop page",
        "content": "Welcome to the shop page"
    }
    return render(request, "home_page.html", context)
