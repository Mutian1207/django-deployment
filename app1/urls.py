from django.conf.urls import url
from django.urls import path
from app1 import views

app_name = "app1"

urlpatterns = [
    
    path('register/',views.register,name = 'register'),
    path('login/',views.log,name='login'),
    path('logout/',views.outlog,name='logout'),

]