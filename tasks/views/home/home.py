from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(request, *args, **kwargs)

