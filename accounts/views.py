from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect 
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout


class UserRegistration(View):
    def get(self,request):
        form=UserRegistrationForm()

        return render(request,'accounts/register.html',{'form':form })


    def post(self,request):
        form=UserRegistrationForm(request.POST)
        
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,'user registered successfuly','success')


        return redirect('home:home')




class UserLogin(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'accounts/login.html',{'form':form})

    def post(self,request):
        form=UserLoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
        # username=request.POST['username'],
        # password=request.POST['password']
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,f'you have loged in successfully {user}' ,'success')


            else:
                raise AuthenticationError('user name or password is incorrect')

        return redirect('home:home' )    



class UserLogout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'you loged out successfully','success')
        return redirect('home:home')