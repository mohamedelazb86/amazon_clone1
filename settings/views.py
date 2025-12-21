from django.shortcuts import render
from django.contrib import messages



def home(request):
    messages.success(request,'مبرروك تم الدخول الى النظام بنجاح')
    return render(request,'settings/home.html',{})
