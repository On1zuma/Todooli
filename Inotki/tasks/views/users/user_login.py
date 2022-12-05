from django.contrib.auth.views import LoginView
from django.urls import reverse


class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tasks')
