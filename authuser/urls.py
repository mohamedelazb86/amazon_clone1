from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='authuser'

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('all_user',login_required(views.all_user),name='all_user'),
    path('active_deactive/<int:id>/', views.active_deactive, name='active_deactive'),

]
