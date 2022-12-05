from django.views.generic import DeleteView

from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = "tasks/task_delete.html"

    def get_success_url(self):
        return reverse('tasks')

    def __str__(self):
        return 'Memo={0}, Tag={1}'.format(self.memo, self.tags)