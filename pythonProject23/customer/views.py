from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import *
#from . import loaddata
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
from product.models import *




#@login_required
def profileUpdate(request):
    if (request.method == "POST"):
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST,instance=request.user)
        if (user_update_form.is_valid() and profile_update_form.is_valid()):
        #if (user_update_form.is_valid()):
            user_update_form.save()
            profile_update_form.save()
            return redirect('profile')
        else:
            context = {
                'user_update_form': user_update_form,
                'profile_update_form': profile_update_form

            }
            return render(request, 'customer/profileUpdate.html', context)

    else:
        user_update_form = UserUpdateForm()
        profile_update_form = ProfileUpdateForm()
        context = {
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form

        }
        return render(request, 'customer/profileUpdate.html', context)



def stock(request):
    print("enter")
    products = Products.objects.filter(tracking_number='1')
    for p in products:
        print(p.p_name)

    return redirect('home')



def profile(request):
    user=get_user(request)

    context={
        'name':user.username,
        'email':user.email
    }
    return render(request,'customer/profile.html',context)





def register(request):
    if (request.method=="POST"):
        form=UserRegistrationForm(request.POST)
        profileform = RegistrationProfileForm(request.POST)
        #if (form.is_valid() and profileform.is_valid()):
        if (form.is_valid()):
            #error=''
            #dict=request.POST
            #username=dict['username']
            #check=User.objects.filter(username='username')
            #if len(check)==0:
            form.save()
            #profileform.save()

            #else:
                #error='Username already exists.'
                #return render(request, 'customer/register.html', {'form':form,'error':error})

            user = get_user(request)
            #username='Naima'
            #username=form.cleaned_data.get(user.username)
            #password='uap123456'
            #password = form.cleaned_data.get(user.password)
            #new_user=authenticate(username=username,password=password)
            #login(request,new_user)

            #message='Welcome to Inventory Management System'
            #messages.success(request, message=message)
            return redirect('home')
        else:
            context={
                'form':form
            }
            return render(request, 'customer/register.html', context)

    else:
        form = UserRegistrationForm()
        profileform=RegistrationProfileForm()
        #return render(request, 'customer/register.html', {'form':form,'profileform':profileform})
        return render(request, 'customer/register.html', {'form': form})

    #return render(request, 'user/register.html', {'form':form})



@login_required
def home(request):
    return render(request,'customer/home.html')

def adminHome(request):
    return render(request,'customer/adminHome.html')

def customerHome(request):
    return render(request,'product/productList.html')

def empHome(request):
    return render(request,'customer/empHome.html')


def base(request):
    return render(request,'customer/base.html')



