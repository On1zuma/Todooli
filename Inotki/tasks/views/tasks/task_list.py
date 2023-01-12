from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.task import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        global yesterday, precedent_time, today, tomorrow, next_time

        context = super().get_context_data(**kwargs)
        context['show_completed_task'] = self.request.user.option.show_completed_task

        if self.request.user.is_staff:
            context['admin'] = 'Admin dashboard'
            context['tasks_completed'] = context['tasks'].filter(complete=True).order_by('-creation_date')
            context['tasks_not_completed'] = context['tasks'].filter(complete=False).order_by('-creation_date')
            context['tasks'] = context['tasks']
            context['tasks_to_do'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False)

        # if the user is not an admin, then we filter the data
        if not self.request.user.is_staff:

            # data filtered by days
            # today
            today = date.today()
            # coming
            tomorrow = today + timedelta(1)
            next_time = today + timedelta(100000)
            # past
            yesterday = today - timedelta(-1)
            precedent_time = today + timedelta(-100000)

            context['tasks_to_do_late'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__range=(precedent_time, yesterday))

            context['tasks_to_do_today'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day)

            context['tasks_to_do_next_weeks'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__range=(tomorrow, next_time))

            context['tasks_not_completed_no_date'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=True)

            context['tasks_to_do'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .order_by('-creation_date')

            context['tasks_completed'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=True)\
                .order_by('-creation_date')

            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(complete=False).count

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            if self.request.user.is_staff:
                context['tasks_completed'] = context['tasks'].filter(title__icontains=search_input)
                context['tasks_not_completed'] = context['tasks'].filter(title__icontains=search_input)
            else:
                context['tasks_completed'] = context['tasks'].filter(title__icontains=search_input) \
                    .filter(user=self.request.user).filter(complete=True)\
                    .order_by('-creation_date')

                context['tasks_to_do_late'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__range=(precedent_time, yesterday)) \
                    .filter(title__icontains=search_input)

                context['tasks_to_do_today'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day) \
                    .filter(title__icontains=search_input)

                context['tasks_to_do_next_weeks'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__range=(tomorrow, next_time)) \
                    .filter(title__icontains=search_input)

                context['tasks_not_completed_no_date'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=True) \
                    .filter(title__icontains=search_input)

                context['tasks_to_do'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(title__icontains=search_input)

        context['search_input'] = search_input

        return context
