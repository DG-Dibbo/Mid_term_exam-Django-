from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'base.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = forms.RegisterForm()
        return render(request,'signup.html',{'form':form})
    else:
        return render('login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=name, password=user_pass)

                if user is not None:
                    login(request, user)
                    return redirect('profile')
            messages.error(request, "❌ Incorrect username or password! Try again or sign up.")
            return redirect('login') 
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    return redirect('profile')

    
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Updated Successfully')
                form.save()
                # return redirect('profile')
        else:
            form = forms.change_data(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect('signup')
def user_logout(request):
    logout(request)
    return redirect('login')
    
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password changed successfully!")
                return redirect('profile')
            else:
                return render(request, 'passchange.html', {'form': form}) 
        else:
            form = SetPasswordForm(user=request.user)
            return render(request, 'passchange.html', {'form': form}) 
        
    else:
        return redirect('login')


def user_change_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Updated Successfully')
                form.save()
                # return redirect('profile')
        else:
            form = forms.change_data(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect('signup')

# def user_change_data(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = forms.change_data(request.POST, instance=request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, '✅ Your account has been updated successfully!')
#                 return redirect('profile')  # আপডেট হওয়ার পর profile পেজে পাঠাবে
#         else:
#             form = forms.change_data(instance=request.user)  # ✅ ফর্ম লোড করার সময় instance সেট করা হয়েছে

#         return render(request, 'profile.html', {'form': form})  # ✅ profile.html এ ফর্ম পাঠানো হবে
#     else:
#         return redirect('signup')
