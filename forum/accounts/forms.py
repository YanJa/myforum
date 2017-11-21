from django import forms
from django.contrib.auth.models import User


class AccountsForm(forms.ModelForm):
    """
    form校验表单输入
    """

    class Meta:
        model = User
        fields = ["username", "email", "password"]
