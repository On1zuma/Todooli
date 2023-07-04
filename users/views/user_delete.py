from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import DeleteView

from tasks.models.task import Task
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'User'
    template_name = "base/user_delete.html"

    def get(self, request, *args, **kwargs):
        userObject = User.objects.get(pk=kwargs['pk'])

        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)
        else:
            if userObject.username != str(self.request.user):
                return redirect('option_update')  # TODO: 404 page
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        userObject = User.objects.get(pk=self.object.id)

        if self.request.user.is_staff:
            messages.success(self.request, f'Your account has been deleted')
            return super().form_valid(form)

        if userObject.id != self.request.user.id:
            messages.error(self.request, f'You are not allowed to do that')
            return super().form_invalid(form)

        messages.success(self.request, f'Your account has been deleted')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
