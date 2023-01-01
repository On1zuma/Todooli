from django.db import models
from django.contrib.auth.models import User


class Option(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_completed_task = models.BooleanField(default=True)
    instant_deletion = models.BooleanField(default=False)
    email_notification = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    private_profile = models.BooleanField(default=False)
    disable_tag = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} option'
