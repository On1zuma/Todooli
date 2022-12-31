from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse
from users.forms.forms import OptionUpdateForm
from django.contrib import messages


class OptionUserView(LoginRequiredMixin, FormView):
    template_name = 'base/option_update.html'
    form_class = OptionUpdateForm

    def form_valid(self, form):

        if self.request.method == 'POST':
            o_form = OptionUpdateForm(self.request.POST, self.request.FILES,
                                    instance=self.request.user)

            if o_form is not None and o_form.is_valid():
                o_form.save()

                messages.success(self.request, f'Your parameters have been updated!')
                return super().form_valid(form)

            else:
                messages.success(self.request, f'Sorry, an error occurred while submitting your form. Please check '
                                               f'the information entered and try again. If the problem persists, '
                                               f'please contact customer service for assistance.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('tasks')

    def get_context_data(self, **kwargs):
        o_form = OptionUpdateForm(instance=self.request.user)
        context = {
            'o_form': o_form,
        }
        return context
