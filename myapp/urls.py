from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_in", views.logged_inn, name="loging_in"),
]
