from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.task import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['admin'] = 'Admin dashboard'
        # if the user is not an admin, then we filter the data
        if not self.request.user.is_staff:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(complete=False).count

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        context['search_input'] = search_input

        return context
