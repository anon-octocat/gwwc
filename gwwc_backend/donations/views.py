from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def index(request):
    if not request.user.is_authenticated:
        return redirect(f'{settings.LOGIN_URL}?next={request.path}')

    if hasattr(request.user, "income"):
        income = request.user.income
    else:
        income = "Please enter an income"
    if hasattr(request.user, "pledge"):
        pledge = request.user.pledge
    else:
        pledge = "Please enter an pledge"
    donations = request.user.donation_set.all()
    print("hello1", donations)
    context = {
        "name": request.user.first_name,
        "income": income.amount,
        "pledge": pledge.percentage,
        "donations": donations
    }
    return render(request, "donations/index.djhtml", context)


def logout(request):
    auth_logout(request)
    return redirect(f'{settings.LOGIN_URL}')
