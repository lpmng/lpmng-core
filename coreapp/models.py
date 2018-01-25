from django.contrib.auth.models import AbstractUser
from django.db import models

import ldapdb.models


class User(AbstractUser):
    cotisant = models.BooleanField(default=False)
    nbSessions = models.IntegerField(default=0)
    tel = models.CharField(max_length=20, default="")
