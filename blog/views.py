# coding=utf-8

from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from models import POST

# Create your views here.

def index(request):
    posts = POST.objects.order_by('-created_date')
    return render(request,'home.html', {'city':'Альметьевск','posts':posts})

def show_post(reguest):
    post_id=reguest.GET["id"]
    post=POST.objects.get(id=post_id)
    return render(reguest,'show_post.html',{'post':post})


def register(request):
    error = ''
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email != '' and password != '':
            user = User.objects.create(username=email, email=email, password=password)
            return render(request, 'finish_reg.html',{'user': user})
        else:
            error = 'Неправильный логин или пароль'
    return render(request, 'home.html', {'error': error})






def login(request):
    error = ''
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email != '' and password != '':
            user = auth.authenticate(username=email, password =password)
            print user
            print email
            print password
            if user != None:
                auth.login(request, user)
                return HttpResponseRedirect('/')

        error = 'Неправильный логин или пароль'
    return render(request, 'login.html', {'error': error})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
