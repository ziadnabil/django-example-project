from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import request
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm

# Create your views here.

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")

        try:
            user = User.objects.create_user(username, email, password1, password2)
        except:
            user = None
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            request.session["register_error"] = 1

    return render(request, "forms.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session["attempt"] = attempt + 1
            # return redirect("/invalied-password")
            request.session["invalid_user"] = 1

    return render(request, "forms.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login")
