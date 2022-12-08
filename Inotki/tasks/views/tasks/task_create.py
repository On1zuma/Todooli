from django import forms
from django.views.generic import CreateView

from tasks.forms.date_input import DateInputForm
from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = DateInputForm

    #def get_form(self, **kwargs):
    #  form = super(TaskCreate, self).get_form()
    #   form.fields['date_to_do'].widget = forms.SelectDateWidget()
    #    return form

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
