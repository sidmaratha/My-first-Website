from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'variable1' : "This is sent",

        'variable2' : "sid is greate"
    }
    return render(request,'home.html', context)
    

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent', {'output':"saved"})
        return render(request,'result.html')
    else:
        return render(request,'contact.html')
   



