from datetime import timedelta, date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models.tag import Tag
from tasks.models.task import Task


def get_notif(request, **kwargs):

    tasks = Task.objects
    tags = Tag.objects

    if request.user.is_authenticated:
        global yesterday, precedent_time, today, tomorrow, next_time

        notification_obj = Task.objects.filter(user=request.user)
        tag_obj = Tag.objects.filter(user=request.user)

        # data filtered by days
        # today
        today = date.today()
        # coming
        tomorrow = today + timedelta(1)
        next_time = today + timedelta(100000)
        # past
        yesterday = today + timedelta(-1)
        precedent_time = today + timedelta(-100000)

        # Notification PAST TASK + TODAY TASK
        notifCount = notification_obj.filter(user=request.user, complete=False, date_to_do__isnull=False,
                                             date_to_do__lt=today).count()
        notifCount += notification_obj.filter(user=request.user, complete=False, date_to_do__isnull=False,
                                              date_to_do__year=today.year, date_to_do__month=today.month,
                                              date_to_do__day=today.day).count()

        taskCount = notification_obj.filter(user=request.user).count()
        taskCountCompleted = notification_obj.filter(user=request.user, complete=True).count()
        tagCount = tag_obj.filter(user=request.user).count()

        globalTaskCount = tasks.count()
        globalTaskCountCompleted = tasks.filter(complete=True).count()
        globalTagCount = tags.count()

        return {
            'notifCount': notifCount,
            'taskCount': taskCount,
            'taskCountCompleted': taskCountCompleted,
            'tagCount': tagCount,

            'globalTaskCount': globalTaskCount,
            'globalTaskCountCompleted': globalTaskCountCompleted,
            'globalTagCount': globalTagCount,
        }
    else:
        globalTaskCount = tasks.count()
        globalTaskCountCompleted = tasks.filter(complete=True).count()
        globalTagCount = tags.count()

        return {
            'globalTaskCount': globalTaskCount,
            'globalTaskCountCompleted': globalTaskCountCompleted,
            'globalTagCount': globalTagCount,
        }
