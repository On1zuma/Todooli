from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from django.urls import reverse
from users.forms.forms import UserUpdateForm, ProfileUpdateForm
from users.models.users import Profile
from django.contrib import messages


class UpdateView(LoginRequiredMixin, FormView):
    template_name = 'base/profile.html'
    model = Profile

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')

    def get_context_data(self, **kwargs):
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return context
