from django.shortcuts import render, redirect
from todo_app.models import Task


def add_view(request):
    if request.method == "GET":
        return render(request, 'create_task.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline': request.POST.get('deadline')
    }
    task = Task.objects.create(**task_data)
    return redirect(f"/task/?pk={task.pk}")

def detail_view(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    return render(request, 'task.html', context={'task': task})