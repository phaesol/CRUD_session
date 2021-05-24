from django.core.checks import messages
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method=="POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username= request.POST['username'],
                password = request.POST['password1']
            )
            user.save()
            auth.login(request,user)
            return redirect('index')
    else:
        return render(request,'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            message = "아이디 비번 틀림. 확인 요망"
            return render(request,'login.html',{'message':message})
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')