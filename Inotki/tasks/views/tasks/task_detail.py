from django.views.generic import DetailView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = 'task'
