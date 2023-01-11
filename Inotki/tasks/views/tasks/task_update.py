from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView

from tasks.form.date_input import DateInputForm
from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = DateInputForm

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

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
            return redirect('tasks')  # TODO: 404 page

        # complete / not complete
        if 'key_id' in self.kwargs:
            if task.complete:
                task.complete = False
            else:
                task.complete = True
            task.save()
            return redirect('tasks')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        task = Task.objects.get(pk=self.object.id)

        # if staff user and the data don't is not assigned to any user (normally not possible)
        if self.request.user.is_staff and self.object.user is None:
            form.instance.user = self.request.user
            messages.success(self.request, f'Your task has been updated')
            return super().form_valid(form)

        # if staff user and the data does not belong to the admin
        if self.request.user.is_staff:
            messages.success(self.request, f'Your task has been updated')
            return super().form_valid(form)

        # if the task is not assigned to the user who is editing the task
        if form.instance.user is not None:
            if task.user != form.instance.user or task.user != self.request.user:
                messages.error(self.request, f'You are not allowed to do that')
                return super().form_invalid(form)

        if task.user != self.request.user:
            messages.error(self.request, f'You are not allowed to do that')
            return super().form_invalid(form)

        # name of passed object   #name of the user session
        form.instance.user = self.request.user
        messages.success(self.request, f'Your task has been updated')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
