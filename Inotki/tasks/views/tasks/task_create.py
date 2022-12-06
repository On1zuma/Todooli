from django.views.generic import CreateView

from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ['title', 'description', 'date_to_do', 'complete']

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
