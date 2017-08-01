from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def index(request):
    if not request.user.is_authenticated:
        return redirect(f'{settings.LOGIN_URL}?next={request.path}')

    if hasattr(request.user, "income"):
        income = request.user.income.amount
    else:
        income = "Please enter an income"
    if hasattr(request.user, "pledge"):
        pledge = request.user.pledge.percentage
    else:
        pledge = "Please enter an pledge"
    donations = request.user.donation_set.all()
    context = {
        "name": request.user.first_name,
        "income": income,
        "pledge": pledge,
        "donations": donations
    }
    return render(request, "donations/index.djhtml", context)


def api(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    context = {
        "name": request.user.first_name,
        "income": request.user.income.amount,
        "pledge": request.user.pledge.percentage,
        "donations": [donation.serialize()
                      for donation in request.user.donation_set.all()]
    }
    return render(request, "donations/api.djjson", context)


def logout(request):
    auth_logout(request)
    return redirect(f'{settings.LOGIN_URL}')
