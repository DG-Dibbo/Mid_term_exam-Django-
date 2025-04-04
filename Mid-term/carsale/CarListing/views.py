from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DetailView
from django.contrib.auth.views import LoginView
from . import models


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account Created Successfully')
                return redirect('login')
        else:
            form = forms.RegistrationForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success = (self.request,'Logged in Successfully')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.success = (self.request,'Logged in information Incorrect')
        return super().form_invalid(form)

def profile(request):
    purchase = models.CarPurchase.objects.filter(user=request.user)
    return render(request,'profile.html',{'purchase':purchase})      

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password has been changed')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')
    
def user_change_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance= request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Account Updated Successfully')
                # return redirect('profile')
        else:
            form = forms.change_data(instance = request.user)
        return render(request,'edit_profile.html',{'form':form})
    else:
        return redirect('login')

@method_decorator(login_required,name='dispatch')
class AddCarCreateView(CreateView):
    model = models.CarModel
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('carsale')
    def form_valid(self, form):
        form.instance.brand = form.cleaned_data['brand']
        return super().form_valid(form)
    
class ReadCarDetailView(DetailView):
    model = models.CarModel
    template_name = 'read_car.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['read'] = self.object
        context['comments'] = self.object.comments.all()
        context['comment_form'] = forms.commentForm()
        return context
   
def commentPeople(request, id):
    car_model = get_object_or_404(models.CarModel, id=id)
    if request.method == "POST":
        comment_form = forms.commentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_model = car_model
            new_comment.save()

    return redirect('read_car', id=id) 

@login_required
def buy_car(request, id):
    # Retrieve the car object
    car = get_object_or_404(models.CarModel, pk=id)

    # Check if the user has already purchased this car
    if not models.CarPurchase.objects.filter(user=request.user, carModel=car).exists():
        # Create a new CarPurchase record
        models.CarPurchase.objects.create(user=request.user, carModel=car)
        car.quantity -= 1
        car.save()
    return redirect('profile')

    

