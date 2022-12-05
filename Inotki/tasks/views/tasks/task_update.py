from django.urls import reverse
from django.views.generic import UpdateView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ['title', 'description', 'complete']

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)