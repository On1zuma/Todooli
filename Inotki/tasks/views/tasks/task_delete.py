from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DeleteView

from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = "tasks/task_delete.html"

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)

        if task.user != self.request.user:
            return redirect('tasks')  # TODO: 404 page
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        task = Task.objects.get(pk=self.object.id)

        if self.request.user.is_staff:
            messages.success(self.request, f'Succes, your task has been deleted', 'success')
            return super().form_valid(form)

        if task.user != self.request.user:
            messages.success(self.request, f'You are not allowed to do that', 'danger')
            return super().form_invalid(form)

        messages.success(self.request, f'Succes, your task has been deleted', 'success')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
