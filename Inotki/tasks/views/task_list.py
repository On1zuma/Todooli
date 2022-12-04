from django.shortcuts import render
from django.views.generic import ListView

from tasks.models.task import Task


class TaskList(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = 'tasks'
