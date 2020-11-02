from django.contrib.auth import auth, authenticate, login, logout
from django.http import request
from django.shortcuts import redirect, render
from .forms import LoginForm

# Create your views here.


def login_view(request):
    form = LoginForm(request.Post or None)
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


def logut_view(request):
    logout(request)
    return redirect("/login")
