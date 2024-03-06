from django.urls import path,include
from hospitalmgtapp import views

urlpatterns = [
    path('',views.index),
    path('base',views.base),
    
]