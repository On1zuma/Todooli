from django.db import models
from django.contrib.auth.models import User

from tasks.models.group import Group
from tasks.models.tag import Tag


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    date_to_do = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks_tags', blank=True)
    group = models.ManyToManyField(Group, related_name='tasks_groups', blank=True)

    class Meta:
        ordering = ['date_to_do']

    def __str__(self):
        return str(self.title) if self.title else ''


