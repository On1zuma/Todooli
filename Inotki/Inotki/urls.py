"""Inotki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tasks.views.tasks.task_create import TaskCreate
from tasks.views.tasks.task_delete import TaskDelete
from tasks.views.tasks.task_detail import TaskDetail
from tasks.views.tasks.task_list import TaskList
from tasks.views.tasks.task_update import TaskUpdate

from tasks.views.users.user_login import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    #Users
    path('user/login/', UserLoginView.as_view(), name='login'),

    # Tasks
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),

]
