from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.task import Task


def get_notif(request, **kwargs):
    if request.user.is_authenticated:
        global yesterday, precedent_time, today, tomorrow, next_time

        notification_obj = Task.objects.filter(user=request.user)

        # data filtered by days
        # today
        today = date.today()
        # coming
        tomorrow = today + timedelta(1)
        next_time = today + timedelta(100000)
        # past
        yesterday = today + timedelta(-1)
        precedent_time = today + timedelta(-100000)

        notifCount = notification_obj.filter(user=request.user, complete=False, date_to_do__isnull=False,
                                             date_to_do__range=(precedent_time, yesterday)).count()
        notifCount += notification_obj.filter(user=request.user, complete=False, date_to_do__isnull=False,
                                              date_to_do__year=today.year, date_to_do__month=today.month,
                                              date_to_do__day=today.day).count()

        return {'notifCount': notifCount}
    return {}
