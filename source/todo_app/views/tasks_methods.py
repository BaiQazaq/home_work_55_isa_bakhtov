from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task


def add_view(request):
    if request.method == "GET":
        return render(request, 'create_task.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline': request.POST.get('deadline')
    }
    task = Task.objects.create(**task_data)
    return redirect('show', pk=task.pk)

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})

def update_view(request, pk):
    errors = {}
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        if not request.POST.get('title'):
            errors['title'] = 'Title field is required'
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline =request.POST.get('deadline')
        task.status =request.POST.get('status')
        if errors:
            return render(
        request,
        'update_task.html',
        context={
            'task': task, 
            'errors': errors
            })
        task.save()
        return redirect('show', pk=task.pk)
    return render(
        request,
        'update_task.html',
        context={
            'task': task, 
            'errors': errors
            })
