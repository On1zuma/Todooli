from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag_name = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.tag_name}, {self.user}' or 'empty'
