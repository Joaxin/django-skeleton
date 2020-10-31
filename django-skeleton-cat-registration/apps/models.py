from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class MyApps(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True, null=True
    )