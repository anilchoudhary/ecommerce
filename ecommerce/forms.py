from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "Enter your fullname..."}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "Enter your email..."}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control",
               "placeholder": "Enter your message..."}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='confirm password', max_length=32, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username has taken")
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email has taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if (password2 != password):
            raise forms.ValidationError("Password must match.")
        return data
