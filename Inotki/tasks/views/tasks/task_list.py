from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from tasks.models.tag import Tag
from tasks.models.task import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        global yesterday, long_time_ago, today, tomorrow, next_time

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
            yesterday = date.today() - timedelta(days=1)
            long_time_ago = date(1000, 1, 1)

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

            context['tasks_to_do_next_weeks'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__gte=tomorrow)

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
                .filter(complete=True) \
                .order_by('-creation_date')

            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(complete=False).count

            tag_list = Tag.objects.filter(user=self.request.user)
            context['tag_list'] = tag_list

        # filter:
        search_input = self.request.GET.get('search-area') or ''
        tag_input = self.request.GET.get('tag-area') or ''

        tags = Tag.objects.filter(tag_name__icontains=search_input)

        if search_input:
            if self.request.user.is_staff:
                context['tasks_completed'] = context['tasks'].filter(title__icontains=search_input)
                context['tasks_not_completed'] = context['tasks'].filter(title__icontains=search_input)
            else:
                context['tasks_completed'] = context['tasks'] \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags)) \
                    .filter(user=self.request.user).filter(complete=True) \
                    .order_by('-creation_date')

                context['tasks_to_do_late'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__lt=today) \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags))

                context['tasks_to_do_today'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day) \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags))

                context['tasks_to_do_next_weeks'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=False) \
                    .filter(date_to_do__gte=tomorrow) \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags))

                context['tasks_not_completed_no_date'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(date_to_do__isnull=True) \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags))

                context['tasks_to_do'] = context['tasks'] \
                    .filter(user=self.request.user) \
                    .filter(complete=False) \
                    .filter(Q(title__icontains=search_input) | Q(tags__in=tags))

        if tag_input:
            # check if the given tag correspond
            tag_objects = Tag.objects.filter(tag_name__icontains=tag_input)

            context['tasks_completed'] = context['tasks'] \
                .filter(tags__in=tag_objects) \
                .filter(user=self.request.user).filter(complete=True) \
                .order_by('-creation_date')

            context['tasks_to_do_late'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__lt=today) \
                .filter(tags__in=tag_objects)

            context['tasks_to_do_today'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__year=today.year, date_to_do__month=today.month, date_to_do__day=today.day) \
                .filter(tags__in=tag_objects)

            context['tasks_to_do_next_weeks'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=False) \
                .filter(date_to_do__gte=tomorrow) \
                .filter(tags__in=tag_objects)

            context['tasks_not_completed_no_date'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(date_to_do__isnull=True) \
                .filter(tags__in=tag_objects)

            context['tasks_to_do'] = context['tasks'] \
                .filter(user=self.request.user) \
                .filter(complete=False) \
                .filter(tags__in=tag_objects)

        context['tag_input'] = tag_input
        context['search_input'] = search_input

        return context
