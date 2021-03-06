from django import forms
from .models import Schedule
import bootstrap_datepicker_plus as datetimepicker


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['summary', 'date', 'place', 'time', 'detail']
        widgets = {
            'date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'time': datetimepicker.TimePickerInput(
                format='%H:%M',
                options={
                    'locale': 'ja',
                }
            ),
        }
