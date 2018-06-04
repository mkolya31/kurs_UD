from django.contrib import auth
from django.shortcuts import redirect, render
from django.conf import settings


def getting_username(request):

    username = auth.get_user(request).username

    return locals()
