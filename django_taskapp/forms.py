from django import forms


class RegistrationTask(forms.Form):
    title = forms.CharField(
        label='summary',
        max_length=50,
    )
    field = forms.CharField(
        label='place',
        max_length=10,
    )
