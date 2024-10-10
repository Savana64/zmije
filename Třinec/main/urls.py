from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),  
    path('news/', views.news, name='news'),  
    path('municipality/', views.municipality, name='municipality'),  
    path('contacts/', views.contacts, name='contacts'),  
    path('messages/', views.messages, name='messages'), 
]