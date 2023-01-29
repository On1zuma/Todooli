from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import FormView

from users.forms.forms import UserRegisterForm
from django.core.mail import EmailMessage

from users.tokens import account_activation_token


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')


def activateEmail(request, user, to_email):
    mail_subject = "Igonii - Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Please, check your email to activate your account')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


class RegisterView(FormView):
    template_name = 'base/user_register.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tasks')

    def form_valid(self, form):
        # if form valid we register the user
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(self.request, user, form.cleaned_data.get('email'))
            return redirect('account_activation')
        else:
            messages.error(self.request, f'An error occurred while submitting the form')
            return super().form_invalid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)
