from django.db import models
import string
import random
# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(primary_key=True, max_length=254)
    email_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return self.email
