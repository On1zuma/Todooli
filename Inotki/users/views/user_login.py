from captcha.fields import ReCaptchaField
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from users.forms.forms import UserLoginForm


class UserLoginView(FormView):
    template_name = 'base/user_login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        # if form valid we register the user
        form = AuthenticationForm(request=self.request, data=self.request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(self.request, user)
                messages.success(self.request, f'Welcome back {user.username} !')

            return redirect('tasks')
        else:
            messages.success(self.request, f'An error occurred while submitting the form')
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('tasks')
