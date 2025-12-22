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


def add_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        active = request.POST.get('is_active') == 'on'
        full_name=request.POST.get('full_name')
        job=request.POST.get('job')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        image=request.FILES.get('image')

        if User.objects.filter(username=username).exists():
            messages.error(request,'معذرة هذا المستخدم موجود سابقا')
            return redirect('authuser:add_user')

        user=User.objects.create(
            username=username,
            is_active=active,
            is_staff=active,
            full_name=full_name,
            job=job,
            email=email,
            phone=phone

        )
        user.set_password(password)
        user.image=image
        user.save()
        messages.success(request,'مبررروووك تم الحفظ بنحاج')
        return redirect('authuser:all_user')

    return render(request,'authuser/add_user.html',{})

def edit_user(request,id):
    user=User.objects.get(id=id)
    if request.method == 'POST':
        active=request.POST.get('is_active') == 'on'
        full_name=request.POST.get('full_name')
        job=request.POST.get('job')
        phone=request.POST.get('job')
        image=request.FILES.get('image')

        user.is_active=active
        user.full_name=full_name
        user.job=job
        user.phone=phone
        user.image=image
        user.save()
        messages.success(request,'مبرووك تم التعديل بنجاح')
        return redirect('authuser:all_user')


    context={
        'user':user
    }
    return render(request,'authuser/edit_user.html',context)

def delete_user(request,id):
    user=get_object_or_404(User,id=id)
    user.delete()
    messages.success(request,'تم الحذف بنحاج')
    return redirect('authuser:all_user')
    
