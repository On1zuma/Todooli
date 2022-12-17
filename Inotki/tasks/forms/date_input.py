from django import forms
from django.forms import ModelForm

from tasks.models.task import Task


class DateTime(forms.DateTimeInput):
    input_type = 'date'


class DateInputForm(ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'date_to_do', 'complete']
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
