from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import *


def login(request):
    form = ShopUserLoginForm(data=request.POST)
    next_ = request.GET.get('next', '')
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('home'))

    context = {
        "title": "вход",
        "login_form": form,
        "next": next_
    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_email(user):
                print(f'register {user.username} success')
            else:
                print(f'register {user.username} fail')
            return HttpResponseRedirect(reverse('auth:login'))

    context = {
        "title": "регистрация",
        "register_form": form,
    }
    return render(request, 'authapp/register.html', context=context)


def edit(request):
    form = ShopUserEditForm(instance=request.user)
    if request.method == 'POST':
        form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {
        "title": "редактирование",
        "edit_form": form,
    }
    return render(request, 'authapp/edit.html', context=context)


def send_verify_email(user):
    link = reverse('authapp:verify', args=[user.email, user.activation_key])
    subject = f'Подтверждение учётной записи {user.email}'
    message = f'Перейдите по данной ссылке для подтверждения почты и активации акаунта: {settings.BASE_URL}{link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)


def verify(request, email, activation_key):
    user = ShopUser.objects.get(email=email)
    if user.activation_key == activation_key and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = ''
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')