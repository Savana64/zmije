from django.shortcuts import render

def home(request):  
    return render(request, 'main/home.html')  

def news(request):  
    return render(request, 'main/news.html')  

def municipality(request):  
    return render(request, 'main/municipality.html')  

def contacts(request):  
    return render(request, 'main/contacts.html')  

def messages(request):  
    return render(request, 'main/messages.html') 

# Create your views here.
