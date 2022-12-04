from django.db import models
from django.contrib.auth.models import User

from tasks.models.group import Group
from tasks.models.tag import Tag


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    date_to_do = models.DateTimeField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks_tags', blank=True)
    groups = models.ManyToManyField(Group, related_name='tasks_groups', blank=True)

    def __str__(self):
        return self.title


class Meta:
    ordering = ['complete']
