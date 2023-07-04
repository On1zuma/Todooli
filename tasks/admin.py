from django.contrib import admin

from tasks.models.group import Group
from tasks.models.tag import Tag
from tasks.models.task import Task

admin.site.register(Task)
admin.site.register(Group)
admin.site.register(Tag)


