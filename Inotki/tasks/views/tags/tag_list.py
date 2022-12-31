from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.tag import Tag


class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = "tags/tag_list.html"
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tags'] = context['tags'].filter(user=self.request.user)
        context['count'] = context['tags'].filter(user=self.request.user).count

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tags'] = context['tags'].filter(user=self.request.user).filter(tag_name__icontains=search_input)

        context['search_input'] = search_input

        return context
