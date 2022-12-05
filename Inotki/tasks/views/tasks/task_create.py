from django.views.generic import CreateView

from tasks.models.task import Task
from django.urls import reverse

class TaskCreate(CreateView):
    model = Task
    template_name = "task_form.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('tasks')
