from django.contrib import admin
from django.urls import path

from tasks.views.tags.tag_create import TagCreate
#tasks
from tasks.views.tasks.task_create import TaskCreate
from tasks.views.tasks.task_delete import TaskDelete
from tasks.views.tasks.task_detail import TaskDetail
from tasks.views.tasks.task_list import TaskList
from tasks.views.tasks.task_update import TaskUpdate

#users
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from users.views.user_login import UserLoginView
from users.views.user_profile import UserProfileView
from users.views.user_register import RegisterView
from users.views.user_update import UpdateUserView

#url settings (images...)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/update/', UpdateUserView.as_view(), name='profile_update'),
    path('user/profile/', UserProfileView.as_view(), name='profile'),

    # Rest password
    path('reset-password/',
         PasswordResetView.as_view(template_name='base/password/password_reset.html'),
         name='password_reset'),
    path('reset-password/done/',
         PasswordResetDoneView.as_view(template_name='base/password/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='base/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset-password-complete/',
         PasswordResetCompleteView.as_view(template_name='base/password/password_reset_complete.html'),
         name='password_reset_complete'),

    # Task
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),

    #Tag
    path('tag/create/', TagCreate.as_view(), name='tag_create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

