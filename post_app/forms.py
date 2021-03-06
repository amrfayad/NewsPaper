
from django import forms
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+\s\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.RegexField(regex=r'^\w+@\w+.\w{3}$',widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"),error_messages={ 'invalid': _("Email must have @ and . then 3 chars") })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))


#clean used to validate the form

    def clean (self):
            if 'email' in self.cleaned_data:

                try:
                    user = User.objects.get(email=self.cleaned_data['email'])

                except User.DoesNotExist:

                        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                            raise forms.ValidationError(_("The two password fields did not match."))
                        return self.cleaned_data
                raise forms.ValidationError(_("Email Already Exist"))






