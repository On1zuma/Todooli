from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from users.forms.forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'base/user_register.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        # if form valid we register the user
        global user
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            messages.info(self.request, f'Welcome {username} ')

        if user is not None:
            login(self.request, user)
            return super(RegisterView, self).form_valid(form)
        return redirect('register')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)
