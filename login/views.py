from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def user_login(request):
    """Authenticate a user."""
    # Etape 1 :
    email = username = request.POST.get("email-or-username")
    password = request.POST.get("password")

    # Etape 2 :
    user = authenticate(request, email=email, username=username, password=password)

    # Etape 3 :
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
    else:
        messages.add_message(
            request, messages.ERROR, "Les champs renseignés sont invalides."
        )

    return redirect("")


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous êtes déconnecté !")
    return redirect("")
