from django.views import View
from django.views.generic import DetailView, TemplateView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "base/profile.html"
