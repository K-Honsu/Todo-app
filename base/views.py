from django.shortcuts import render, redirect
from .models import Task
from .forms import *

# Create your views here.

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
