from django.contrib import admin
from django.urls import path

# tags
from tasks.views.tags.tag_create import TagCreate
from tasks.views.tags.tag_delete import TagDelete
from tasks.views.tags.tag_list import TagList
from tasks.views.tags.tag_update import TagUpdate

# tasks
from tasks.views.tasks.task_create import TaskCreate
from tasks.views.tasks.task_delete import TaskDelete
from tasks.views.tasks.task_detail import TaskDetail
from tasks.views.tasks.task_list import TaskList
from tasks.views.tasks.task_update import TaskUpdate

# users
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from users.views import user_register
from users.views.option_update import OptionUserView
from users.views.user_account_activation import UserAccountActivation

from users.views.user_delete import UserDelete
from users.views.user_detail import UserDetail
from users.views.user_login import UserLoginView
from users.views.user_profile import UserProfileView
from users.views.user_register import RegisterView
from users.views.user_update import UpdateUserView

# url settings (images...)
from django.conf import settings
from django.conf.urls.static import static

# Notification
from tasks.views.notification.notification_list import NotificationList

# Article
from tasks.views.articles.info import Productivity, GoodTask, UseIt, TermsService, ContactUs, PrivacyPolicy, Gdpr

# Home
from tasks.views.home.home import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/update/', UpdateUserView.as_view(), name='profile_update'),
    path('user/profile/', UserProfileView.as_view(), name='profile'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user'),
    path('user/option/', OptionUserView.as_view(), name='option_update'),
    path('user/delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),

    path('activate/<uidb64>/<token>', user_register.activate, name='activate'),
    path('user/accountActivation/', UserAccountActivation.as_view(), name='account_activation'),

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
    path('task/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('task/completed/<int:pk>/<int:key_id>/', TaskUpdate.as_view(), name='task_completed'),

    # Tag
    path('tag/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/create/c/<int:key_id>/', TagCreate.as_view(), name='tag_create_id'),
    path('tag/create/e/<int:pk>/', TagCreate.as_view(), name='tag_create_pk'),
    path('tag/', TagList.as_view(), name='tags'),
    path('tag/update/<int:pk>/', TagUpdate.as_view(), name='tag_update'),
    path('tag/delete/<int:pk>/', TagDelete.as_view(), name='tag_delete'),

    # Notification
    path('notification/', NotificationList.as_view(), name='notification'),
    path('notification/completed/<int:pk>/<int:tc_id>/', TaskUpdate.as_view(), name='notification_task_completed'),

    # Home
    path('', HomeView.as_view(), name='home'),

    # Article
    path('article/task/', GoodTask.as_view(), name='article-task'),
    path('article/productivity/', Productivity.as_view(), name='article-productivity'),
    path('article/use-it/', UseIt.as_view(), name='article-use-it'),

    # Legal information
    path('contact-us/', ContactUs.as_view(), name='contact-us'),
    path('terms-of-service/', TermsService.as_view(), name='terms-of-service'),
    path('privacy-policy/', PrivacyPolicy.as_view(), name='privacy-policy'),
    path('gdpr/', Gdpr.as_view(), name='gdpr'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
