from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),  
    path('news/', views.news, name='news'), 
    path('news/<str:slug>/', views.news, name='news_with_slug'),
    path('municipality/', views.municipality, name='municipality'),
    path('municipality/<str:slug>/', views.municipality, name='municipality_with_slug'),  
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<str:slug>/', views.contacts, name='contacts_with_slug'),   
    path('messages/', views.messages, name='messages'), 
    path('messages/<str:slug>/', views.messages, name='messages_with_slug'),
    path('history/', views.history, name='history'), 
    path('history/<str:slug>/', views.history, name='history_with_slug'),
    
]