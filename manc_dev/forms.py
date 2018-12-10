from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up','Sign up',css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username','email','password')