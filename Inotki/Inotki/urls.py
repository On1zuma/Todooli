from django.contrib import admin
from django.urls import path

from tasks.views.tasks.task_create import TaskCreate
from tasks.views.tasks.task_delete import TaskDelete
from tasks.views.tasks.task_detail import TaskDetail
from tasks.views.tasks.task_list import TaskList
from tasks.views.tasks.task_update import TaskUpdate

from tasks.views.users.user_login import UserLoginView
from django.contrib.auth.views import LogoutView
from tasks.views.users.user_register import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('user/register/', RegisterView.as_view(), name='register'),

    # Tasks
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
