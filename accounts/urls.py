from django.urls import path
from . import views


app_name='accounts'
urlpatterns=[
    path('registration/',views.UserRegistration.as_view(),name='register'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('logout/',views.UserLogout.as_view(),name='logout'),
    ]