from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
