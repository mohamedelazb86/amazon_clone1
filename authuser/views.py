from django.shortcuts import render,redirect,get_object_or_404
from django.views import  View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import User


class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            messages.error(request,'معذرة انت حاليا داخل النظام')
            return redirect('/')
        return render(request,'authuser/login.html',{})
    



    def post(self,request):
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            next_url=request.POST.get('next')

            if username and password :
                user=authenticate(request,username=username,password=password)
                if user :
                    if user.is_active:
                        login(request,user)
                        messages.success(request,'مبررروووك تم دخول انظام بنجاح')

                        return redirect(next_url or '/')
                    messages.error(request,'معذرة هذا المستخدم غير نشط وغير مسموح له الدخول للنظام')

                messages.error(request,'معذرة هذا المستخدم غير موجود')
            messages.error(request,'معذرة لا يوجد كلمة سر و اسم المستخدم')

        return render(request,'authuser/login.html',{})
    
class LogoutView(View):
    def post(self,request):
        logout(request)
        messages.success(request,'مبرروك تم الخروج من النظام بنجاح')
        return render(request,'authuser/login.html',{})
    
@login_required    
def all_user(request):
    users=User.objects.all()
    context={
        'users':users
    }

    return render(request,'authuser/all_user.html',context)

@login_required

def active_deactive(request,id):
    user=get_object_or_404(User,id=id)
    if user.is_superuser:
        messages.warning(request,'عفوا هذا المستخدم لا يسمح له بالتعديل فيه')
        return redirect('authuser:all_user')
    if user.is_active:
        user.is_active=False
        messages.success(request,'تم الغاء تفعيل هذا المستخدم')
    else:
        user.is_active=True
        messages.success(request,'مبرروك تم تفعيل المستخدم بنجاح')
    user.save()
    return redirect('authuser:all_user')
