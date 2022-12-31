from django.contrib.auth.models import User
from django.views.generic import DetailView
from tasks.models.task import Task
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = "base/user_detail.html"
    context_object_name = 'user_profile'

    def get(self, request, *args, **kwargs):
        user_profile = User.objects.get(pk=kwargs['pk'])

        # We check if the user is an admin
        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)

        # We check if the user is trying to edit their own data
        if user_profile != self.request.user and user_profile.option.private_profile == True:
            return redirect('tasks')  # TODO: 404 page
        return super().get(request, *args, **kwargs)
