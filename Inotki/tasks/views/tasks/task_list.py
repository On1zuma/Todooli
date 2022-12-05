from django.views.generic import ListView

from tasks.models.task import Task


class TaskList(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'
