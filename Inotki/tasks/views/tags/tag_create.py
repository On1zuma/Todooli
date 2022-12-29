from django.views.generic import CreateView

from tasks.form.date_input import DateInputForm
from tasks.models.tag import Tag
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/tag_form.html"
    fields = ['tag_name']

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
