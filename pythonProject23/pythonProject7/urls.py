"""pythonProject7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views as views1
from product import views as viewsprod

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',views1.profile,name='profile'),

    path('register/',views1.register,name='register'),
    path('base/',views1.base),
    path('home/',views1.home,name='home'),
    path('adminHome/',views1.adminHome,name='adminHome'),
    path('customerHome/',views1.customerHome,name='customerHome'),
    path('empHome/',views1.empHome,name='empHome'),

    path('',auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    #path('accounts/profile/',views1.profile),
    path('logout/',auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
    path('pass_change/',auth_views.PasswordChangeView.as_view(template_name='customer/pass_change.html'), name='pass_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='customer/password_change_done.html'), name='password_change_done'),

    path('productList/',viewsprod.productList,name='productList'),

    path('makeinvoice/',viewsprod.makeinvoice,name='makeinvoice'),
    path('addproduct/',viewsprod.addproduct,name='addproduct'),
    path('due/',viewsprod.due,name='due'),
    path('outOfStock/',viewsprod.outOfStock,name='outOfStock'),
    path('clothes/',viewsprod.clothes,name='clothes'),
    path('electronics/',viewsprod.electronics,name='electronics'),
    path('food/',viewsprod.food,name='food'),
    path('order/',viewsprod.order,name='order'),
    path('userorder/',viewsprod.userorder,name='userorder'),
    path('salesReport/', viewsprod.salesReport,name='salesReport'),
    path('stockReport/', viewsprod.stockReport,name='stockReport'),

    path('user_Details/',viewsprod.user_Details,name='user_Details'),

    path('profileUpdate/',views1.profileUpdate,name='profileUpdate'),
    #path('customerInfo/',views1.customerInfo,name='customerInfo'),

    path('invoice/',viewsprod.invoice,name='invoice'),
    path('cancelorder/',viewsprod.cancelorder,name='cancelorder'),




]
