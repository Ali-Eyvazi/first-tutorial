from django.shortcuts import render,get_object_or_404
from django.views import View
# Create your views here.
import datetime
from .models import ToDo

class HomeView(View):

    def get(self,request):
        
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
