from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse
from users.forms.forms import UserUpdateForm, ProfileUpdateForm
from users.models.user import Profile
from django.contrib import messages


class UpdateUserView(LoginRequiredMixin, FormView):
    template_name = 'base/user_update.html'
    form_class = ProfileUpdateForm

    def form_valid(self, form):

        if self.request.method == 'POST':
            u_form = UserUpdateForm(self.request.POST, self.request.FILES,
                                    instance=self.request.user)
            p_form = ProfileUpdateForm(self.request.POST, self.request.FILES,
                                       instance=self.request.user.profile)

            if u_form is not None and p_form is not None and u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()

                messages.success(self.request, f'Your account has been updated!')
                return super().form_valid(form)

            else:
                messages.success(self.request, f'Sorry, an error occurred while submitting your form. Please check '
                                               f'the information entered and try again. If the problem persists, '
                                               f'please contact customer service for assistance.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('profile')

    def get_context_data(self, **kwargs):
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return context
