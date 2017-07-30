from django.contrib import admin

from .models import Donation, Income, Pledge

admin.site.register([Donation, Income, Pledge])
