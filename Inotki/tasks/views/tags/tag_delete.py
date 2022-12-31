from django.shortcuts import redirect
from django.views.generic import DeleteView
from tasks.models.tag import Tag
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tags/tag_delete.html"

    def get(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs['pk'])
        if self.request.user.is_staff:
            return super().get(request, *args, **kwargs)

        if tag.user != self.request.user:
            return redirect('tags')  # TODO: 404 page
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        tag = Tag.objects.get(pk=self.object.id)

        if self.request.user.is_staff:
            messages.success(self.request, f'Succes, your tag has been deleted', 'success')
            return super().form_valid(form)

        if tag.user != self.request.user:
            messages.success(self.request, f'You are not allowed to do that', 'danger')
            return super().form_invalid(form)

        messages.success(self.request, f'Succes, your tag has been deleted', 'success')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tags')
