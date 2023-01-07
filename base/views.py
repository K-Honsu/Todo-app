from django.shortcuts import render
from .models import Task

# Create your views here.

def homePage(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'base/list.html', context)
