from django import forms
from .models import Password

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('site', 'name_site','username', 'password')
        widgets = {
            'site' : forms.URLInput(),
            'name_site' : forms.TextInput(),
            'username' : forms.TextInput(),
            'password': forms.PasswordInput(),
        }