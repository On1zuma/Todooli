from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView

from tasks.forms.date_input import DateInputForm
from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = DateInputForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['admin'] = 'Admin'
        return context

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])

        # We check if the user is an admin
        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)

        # We check if the user is trying to edit their own data
        if task.user != self.request.user:
            # flash message: messages.add
            return redirect('tasks')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        task = Task.objects.get(pk=self.object.id)

        # if staff user and the data does not belong to the admin
        if self.request.user.is_staff and task.user != self.request.user:
            return super().form_valid(form)

        # if staff user and the data don't is not assigned to any user (normally not possible)
        if self.request.user.is_staff and self.object.user is None:
            form.instance.user = self.request.user
            return super().form_valid(form)

        # if the task is not assigned to the user who is editing the task
        if task.user != self.request.user:  # Todo FIX self.object.user is null...
            form.add_error(None, "You can't do that")  # add message to the user that are not supposed to do that
            return super().form_invalid(form)

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
