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
        # If "Instant Delete" is checked, we will delete the form without requiring confirmation.
        # Could be done more neatly.
        elif self.request.user.option.instant_deletion == True and task.user == self.request.user:
            messages.success(self.request, f'Your task has been deleted')
            return self.delete(request, *args, **kwargs)
        else:
            if task.user != self.request.user:
                return redirect('tasks')  # TODO: 404 page
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        task = Task.objects.get(pk=self.object.id)

        if self.request.user.is_staff:
            messages.success(self.request, f'Your task has been deleted')
            return super().form_valid(form)

        if task.user != self.request.user:
            messages.error(self.request, f'You are not allowed to do that')
            return super().form_invalid(form)

        messages.success(self.request, f'Your task has been deleted')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
