from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.task import Task


class NotificationList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "notification/notification_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        global yesterday, precedent_time, today, tomorrow, next_time

        context = super().get_context_data(**kwargs)

        # data filtered by days
        # today
        today = date.today()
        # coming
        tomorrow = today + timedelta(1)
        next_time = today + timedelta(100000)
        # past
        yesterday = today + timedelta(-1)
        precedent_time = today + timedelta(-100000)

        context['tasks_to_do_late'] = context['tasks'] \
            .filter(user=self.request.user) \
            .filter(complete=False) \
            .filter(date_to_do__isnull=False) \
            .filter(date_to_do__lt=today)

        context['tasks_to_do_today'] = context['tasks'] \
            .filter(user=self.request.user) \
            .filter(complete=False) \
            .filter(date_to_do__isnull=False) \
            .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day)

        context['tasks_to_do_late_count'] = context['tasks'] \
            .filter(user=self.request.user) \
            .filter(complete=False) \
            .filter(date_to_do__isnull=False) \
            .filter(date_to_do__lt=today).count

        context['tasks_to_do_today_count'] = context['tasks'] \
            .filter(user=self.request.user) \
            .filter(complete=False) \
            .filter(date_to_do__isnull=False) \
            .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day).count

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks_to_do_today'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day) \
                .filter(title__icontains=search_input)

            context['tasks_to_do_late'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__lt=today) \
                .filter(title__icontains=search_input)

            context['search_input'] = search_input

        return context
