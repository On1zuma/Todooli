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
            return redirect('tasks')  # TODO: faire une page 404 avec un message ou des flash messages
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        task = Task.objects.get(pk=self.object.id)

        if self.request.user.is_staff:
            return super().form_valid(form)

        if task.user != self.request.user:
            return super().form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
