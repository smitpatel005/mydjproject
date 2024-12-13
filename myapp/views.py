from django.shortcuts import render , redirect
from django.http import HttpResponse

from . models import student
from .forms import studentForm

def homepage(request):    
    return HttpResponse('hello django')
def aboutpage(request):
    return render(request,'about.html')
def contactpage(request):
    return render(request,'contact.html')

def addstudent(request):
    if request.method == 'GET':
        context = {'form':studentForm()}
        return render(request,'add.html',context)
    elif request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addstudent)
        else:
            return render(request, 'add.html', {'form': form})
    
