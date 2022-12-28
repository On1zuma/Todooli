from django.contrib import admin
from django.urls import path

#tasks
from tasks.views.tasks.task_create import TaskCreate
from tasks.views.tasks.task_delete import TaskDelete
from tasks.views.tasks.task_detail import TaskDetail
from tasks.views.tasks.task_list import TaskList
from tasks.views.tasks.task_update import TaskUpdate

#users
from django.contrib.auth.views import LogoutView
from users.views.user_login import UserLoginView
from users.views.user_register import RegisterView
from users.views.user_update import UpdateUserView

#url settings (images...)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/update/', UpdateUserView.as_view(), name='profile'),


    # Tasks
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

