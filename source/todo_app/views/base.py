from django.shortcuts import render
from todo_app.models import Task

def base_view(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, 'base.html', context)