from django.views.generic import CreateView

from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('tasks')
