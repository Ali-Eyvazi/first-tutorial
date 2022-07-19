from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    
    
    path('',views.HomeView.as_view(),name='home'),
    path('todos',views.TodoView.as_view(),name='todos'),
    path('delete/<int:id>/',views.DeleteView.as_view(),name='delete'),
    path('update/<int:id>/',views.UpdateView.as_view(),name='update'),
    path('date_creation/',views.Date_creation.as_view(),name='date_creation'),
    path('details/<int:id>/',views.DetailsView.as_view(),name='details'),
    

]



