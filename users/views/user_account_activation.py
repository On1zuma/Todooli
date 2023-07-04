from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserAccountActivation(TemplateView):
    template_name = 'base/user_account_activation.html'
