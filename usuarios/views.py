from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from .forms import RegisterForm


def cadastro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_role(user, "client")
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "usuarios/cadastro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "usuarios/login.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta com sucesso.")
    return redirect("login")