from django.shortcuts import render

def home(request, slug=None):  
    return render(request, 'main/home.html')  

def news(request, slug=None):  
    return render(request, 'main/news.html')  

def municipality(request, slug=None):  
    return render(request, 'main/municipality.html')  

def contacts(request, slug=None):  
    return render(request, 'main/contacts.html')  

def messages(request, slug=None):  
    return render(request, 'main/messages.html')

def history(request, slug=None):  
    return render(request, 'main/history.html') 

# Create your views here.
