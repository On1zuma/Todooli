from django.urls import reverse
from django.views.generic import UpdateView

from tasks.models.task import Task


class TaskUpdate(UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('tasks')
