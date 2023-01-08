from django.contrib import messages
from django.views.generic import CreateView

from tasks.form.date_input import DateInputForm
from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = DateInputForm

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Success, your task has been created', 'success')
        return super().form_valid(form)
