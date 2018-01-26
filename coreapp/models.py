from django.contrib.auth.models import AbstractUser
from django.db import models

import ldapdb.models


class User(AbstractUser):
    cotisant = models.BooleanField(default=False)
    nbSessions = models.IntegerField(default=0)
    tel = models.CharField(max_length=20, default="")


class Session(models.Model):
    mac = models.CharField(max_length=17, unique=True)
    ip4 = models.CharField(max_length=15, unique=True)
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    internet = models.BooleanField(default=True)
