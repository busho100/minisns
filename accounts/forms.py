from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='必須',
        label='苗字'
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='必須',
        label='名前'
    )
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name',  'email', 'password1', 'password2', )