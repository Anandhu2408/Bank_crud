from django import forms
from account.models import account


class Accountform(forms.ModelForm):
    class Meta:
        model=account
        fields='__all__'