import hashlib
import random

from django.contrib.auth import forms
from django.forms import HiddenInput

from authapp.models import ShopUser
import re


class ShopUserLoginForm(forms.AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(forms.UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (re.match(r'[\D]*', first_name) and re.match(r'[\w]*', first_name)):
            raise forms.ValidationError('Имя должно содержать только буквы')
        return first_name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Услуги сайта доступны только пользователям, старше 18 лет')
        return age

    def clean_email(self):
        email = self.cleaned_data['email']
        user = ShopUser.objects.filter(email=email).first()
        if user is not None and user.email != email:
            raise forms.ValidationError('Данный email уже используется другим аккаунтом')
        return email

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()


class ShopUserEditForm(forms.UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (re.fullmatch(r'[\D]*', first_name) and re.fullmatch(r'[\w]*', first_name)):
            raise forms.ValidationError('Имя должно содержать только буквы')
        return first_name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Услуги сайта доступны только пользователям, старше 18 лет')
        return age

    def clean_email(self):
        email = self.cleaned_data['email']
        user = ShopUser.objects.filter(email=email).first()
        if user is not None and user.email != email:
            raise forms.ValidationError('Данный email уже используется другим аккаунтом')
        return email
