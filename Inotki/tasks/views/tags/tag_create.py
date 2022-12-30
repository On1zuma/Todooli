from django.views.generic import CreateView
from tasks.models.tag import Tag
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/tag_form.html"
    fields = ['tag_name']

    def get_success_url(self, **kwargs):
        # go back to previous page depending on if a pk is set up of not (/tag/create/ VS /tag/create/7/)
        if 'pk' in self.kwargs:
            return reverse_lazy('task_update', kwargs={'pk': self.kwargs['pk']})
        return reverse('task_create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
