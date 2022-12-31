from django import forms
from django.forms import ModelForm

from tasks.models.tag import Tag
from tasks.models.task import Task


class DateInputForm(ModelForm):

    # limit choices for tags input
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        new_kwargs = kwargs.get('instance', None)
        if 'instance' in kwargs and new_kwargs is not None:
            self.fields['tags'].queryset = Tag.objects.filter(user=new_kwargs.user.id)
        else:
            self.fields['tags'].queryset = Tag.objects.filter(user=request.user.id)

    class Meta:
        model = Task
        # exclude = ('user',)
        fields = ['user', 'title', 'description', 'date_to_do', 'complete', 'tags']
        widgets = {
            'date_to_do': forms.DateTimeInput(format='%Y-%m-%dT%H:%M',
                                              attrs={'type': 'datetime-local', 'class': 'timepicker'}),
        }

        # widgets = {
        #   'date_to_do': DateTimeInput(attrs={
        #      # 'class': 'datepicker form-control',
        #     # 'id': 'datetimepicker1',
        #    'tabindex': '1',
        #   'placeholder': 'DD/MM/YYYY hh:mm',
        #  'autocomplete': 'on',
        # }, format='dd-mm-YYYY:MM'),
        # }
