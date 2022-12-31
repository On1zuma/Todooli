from django.contrib.auth.models import User
from django.views.generic import DetailView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = "base/user_detail.html"
    context_object_name = 'user_profile'
