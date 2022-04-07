from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMsg

# Create your views here.

def Home(request):
    return render(request, 'home/home.html')

def Service(request):
    return render(request, 'home/service.html')

def Contact(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        comment = data.get('comment')

        if title == '' or email == '':
            context['status'] = 'alert'
            return render(request, 'home/contact.html', context)

        new = ContactMsg()
        new.title = title
        new.email = email
        new.comment = comment
        new.save()

        context['status'] = 'success'

    return render(request, 'home/contact.html', context)