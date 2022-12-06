from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ['user', 'title', 'description', 'date_to_do', 'complete']

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if task.user != self.request.user:
            return redirect('tasks')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if self.object.user != self.request.user:
            form.add_error(None, "You can't do that") #add message to the user that are not supposed to do that
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')
