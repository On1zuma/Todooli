from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return self.tag_name or 'empty'
