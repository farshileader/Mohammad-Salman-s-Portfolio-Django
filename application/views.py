import email
from email import message
import imp
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def showdata(request):
    return render(request, 'showdata.html')    

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        contact= Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse('<h1> Thanks for contacting with us. We will give you a solution immediately, In Sha Allah</h1>')
    return render(request, 'contact.html')



def showdata(request):
    con = Contact.objects.all()
    print(type(con))
    # for i in con:
    #     print(i.id,i.name,i.email,i.message)

    data = {'Contact' : con }

    return render(request, 'showdata.html',data)