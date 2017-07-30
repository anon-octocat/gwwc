from django.http import HttpResponse
# TODO if needed
# from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
