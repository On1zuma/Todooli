from django.views.generic import DetailView

from tasks.models.task import Task


class TaskDetail(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'
