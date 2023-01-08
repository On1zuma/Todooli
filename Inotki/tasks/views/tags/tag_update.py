from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView
from tasks.models.tag import Tag

from django.contrib.auth.mixins import LoginRequiredMixin


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tags/tag_form.html"
    fields = ['tag_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['admin'] = 'Admin'
        return context

    def get(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs['pk'])

        # We check if the user is an admin
        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)

        # We check if the user is trying to edit their own data
        if tag.user != self.request.user:
            return redirect('tags')  # TODO: 404 page
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        tag = Tag.objects.get(pk=self.object.id)

        # if staff user and the data don't is not assigned to any user (normally not possible)
        if self.request.user.is_staff and self.object.user is None:
            form.instance.user = self.request.user
            messages.success(self.request, f'Success, your tag has been updated', 'success')
            return super().form_valid(form)

        # if staff user and the data does not belong to the admin
        if self.request.user.is_staff:
            messages.success(self.request, f'Success, your tag has been updated', 'success')
            return super().form_valid(form)

        # if the task is not assigned to the user who is editing the task
        if form.instance.user is not None:
            if tag.user != form.instance.user or tag.user != self.request.user:
                form.add_error(None, "You can't do that")  # add message to the user that are not supposed to do that
                messages.success(self.request, f'You are not allowed to do that', 'danger')
                return super().form_invalid(form)

        if tag.user != self.request.user:
            form.add_error(None, "You can't do that")  # add message to the user that are not supposed to do that
            messages.success(self.request, f'You are not allowed to do that', 'danger')
            return super().form_invalid(form)

        # name of passed object   #name of the user session
        form.instance.user = self.request.user
        messages.success(self.request, f'Success, your tag has been updated', 'success')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tags')
