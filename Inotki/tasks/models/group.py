from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=200, null=True, blank=True, default='')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.group_name or 'empty'
