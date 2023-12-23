from django.shortcuts import render, redirect 
from . import forms 
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html', {'type' : 'Profile'})

def sign_up(request):
    if request.method == 'POST':
        signup_form = forms.SignupFOrm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "Signed Up Successfully")
            return redirect('login_page')
    else:
        signup_form = forms.SignupFOrm()
    return render(request, 'profile.html', {'form': signup_form,'type':'Sign up'})

def log_in(request):
    if request.method == 'POST':
        log_form = AuthenticationForm(request,request.POST)
        if log_form.is_valid():
            user_name = log_form.cleaned_data['username']
            user_pass = log_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request,user)
                return redirect('profile_page')
            else:
                messages.warning(request,'wrong login information Signup first')
                return redirect('sign_up_page')
    else:
        log_form = AuthenticationForm()

    return render(request,'profile.html', {'form': log_form, 'type': 'Login'})


def log_out(request):
    messages.success(request,'Logout successfully')
    logout(request)
    return redirect('home_page')

@login_required
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            password_form = PasswordChangeForm(request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'password updated successfully')
                update_session_auth_hash(request,password_form.user)
                return redirect('login_page')
        else:
            password_form = PasswordChangeForm(request.user)
            return render(request,'profile.html', {'form': password_form, 'type':'Password Change'})
    else:
        return redirect('login_page')

def password_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form2 = SetPasswordForm(user = request.user, data=request.POST)
            if pass_form2.is_valid():
                pass_form2.save()
                messages.success(request, 'password Set successfully')
                update_session_auth_hash(request,pass_form2.user)
                return redirect('profile_page')
        else:
            pass_form2 = SetPasswordForm(user = request.user)
        return render(request,'profile.html', {'form':pass_form2,'type':'Set Password'})
    else:
        return redirect('login_page')