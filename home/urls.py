from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    
    
    path('',views.HomeView.as_view(),name='home'),
     path('todos',views.TodoView.as_view(),name='todos'),
    path('details/<int:id>/',views.DetailsView.as_view(),name='details')
    

]