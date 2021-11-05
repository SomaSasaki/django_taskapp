from django import forms
from .models import DemoScheduleTable


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = DemoScheduleTable
        fields = '__all__'
