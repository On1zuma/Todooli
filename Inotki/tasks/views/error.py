from django.views import View
from django.views.generic import TemplateView

from tasks.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class errorDetail(TemplateView):
    template_name = "base/error.html"
