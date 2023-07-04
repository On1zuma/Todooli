from django.contrib.auth.models import User
from django.db import models
from tasks.models.tag import Tag


class Group(models.Model):
    user = models.ManyToManyField(User)
    tag = models.ManyToManyField(Tag)

    group_name = models.CharField(max_length=200, null=True, blank=True, default='')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.group_name or 'empty'
