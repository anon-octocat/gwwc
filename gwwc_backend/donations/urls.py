from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^home$", views.index, name="home"),
    url(r"^api$", views.api, name="api"),
    url(r"^accounts/login", auth_views.login,
        {"template_name": "registration/login.djhtml"}, name="login"),
    url(r"^accounts/logout", views.logout, name="logout")
]
