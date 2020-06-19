from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

from . import models


def home(request):
    return render(request, "mytemp/index.html")


def logged_inn(request):

    if request.method == "POST":
        user_n = request.POST.get("user_name")
        user_e = request.POST.get("user_email")
        user_p = request.POST.get("user_password")

        if models.User.objects.filter(user_name=user_n).exists():
            user_name_exists = "User name exists! try difrent."
            front_end_stuff = {"user_name_exist": user_name_exists}

            return render(request, "mytemp/index.html", front_end_stuff)

        elif models.User.objects.filter(email=user_e).exists():
            user_exists = "This email is already exists!"
            front_end_stuff = {"user_exist": user_exists}

            return render(request, "mytemp/index.html", front_end_stuff)

        else:
            models.User.objects.create(user_name=user_n, email=user_e, password=user_p)

            send_mail(
                "Thank You for sign in.",
                f"Hello, {user_n}. Thank you for Sign in. I hop you enjoy Socimid.",
                "your@gmail.com",
                [user_e],
                fail_silently=False,
            )

            return render(request, "mytemp/logged_in.html")

    elif request.method == "GET":
        return HttpResponse("Something went wrong please try agin!")
