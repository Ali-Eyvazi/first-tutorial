from pyexpat.errors import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
# Create your views here.
import datetime
from .models import ToDo
from django.contrib import messages
from .forms import Item_Creation_Form,TodoUpdateForm
class HomeView(View):

    def get(self,request):
        request.user.username
        date=datetime.datetime.now() 
        name='Ali'
        return render(request,'home/home.html',{'name':name,'date':date,})


class DetailsView(View):

    def get(self,request,id):
        todo=get_object_or_404(ToDo,id=id)
        return render(request ,'home/details.html',{'todo':todo})

class TodoView(View):

    def get(self,request):
        todo=ToDo.objects.all()
        return render(request,'home/todos.html',{'models':todo})


class DeleteView(View):
    
    def get(self,request,id):
        
        todo=get_object_or_404(ToDo,id=id)
        todo.delete()

        messages.success(request, ' you deleted item successfully','success')
        return redirect('home:todos')



class Date_creation(View):
    def get(self,request):
        form=Item_Creation_Form()

        return render(request,'home/date_creation.html',{'form':form })



    def post(self,request):

        if request.method =='POST':
            form=Item_Creation_Form(request.POST)

            if form.is_valid():
                cd=form.cleaned_data
                ToDo.objects.create(title=cd['title'],date_time=cd['date_time'],Details=cd['Details'])
            else:
                messages.error(request,'The form\'s fields has been filed wrongly  ','error')
                return redirect('home:home')

            messages.success(request,'date has been created succesfully')
            return redirect('home:todos')

        return redirect('home:home')

class UpdateView(View):
    
    def get(self,request,id):
        todo=ToDo.objects.get(id=id)
        form=TodoUpdateForm(instance=todo)
       
        return render(request,'home/update.html',{'form':form})

    def post(self,request,id):
        todo=ToDo.objects.get(id=id)
        
        form=TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'you have updated your todo ','success')
        return redirect('home:details',id=id)