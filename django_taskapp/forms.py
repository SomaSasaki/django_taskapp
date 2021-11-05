from django import forms
from .models import DemoScheduleTable
import bootstrap_datepicker_plus as datetimepicker


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = DemoScheduleTable
        fields = '__all__'
        widgets = {
            'date': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
