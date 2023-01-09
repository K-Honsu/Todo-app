from django.shortcuts import render, redirect
from .models import Task
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login-page')
def homePage(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'base/list.html', context)


def updatePage(request,pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks':tasks,'form':form}
    return render(request, 'base/edit.html', context)


def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'base/delete.html', context)


def loginPage(request):
    page = 'login-page'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'base/login_page.html', {'page':page})


def logoutPage(request):
    logout(request)
    return redirect('login-page')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            
            if user is not None:
                login(request, user)
                return redirect('/')
    context = {'page':page, 'form':form}
    return render(request, 'base/login_page.html', context)
