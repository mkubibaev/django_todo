from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TodoForm
from webapp.models import Todo


def index_view(request, *args, **kwargs):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})


def todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo.html', {'todo': todo})


def todo_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'add.html', context={'form': form})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                description=form.cleaned_data['description'],
                content=form.cleaned_data['content'],
                status=form.cleaned_data['status'],
                date=form.cleaned_data['date']
            )
            return redirect(todo_view, pk=todo.pk)
        else:
            return render(request, 'add.html', context={'form': form})


def todo_edit_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        form = TodoForm(data={
            'description': todo.description,
            'date': todo.date,
            'status': todo.status,
            'content': todo.content
        })
        return render(request, 'edit.html', context={'form': form, 'todo': todo})
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.description = form.cleaned_data['description']
            todo.date = form.cleaned_data['date']
            todo.status = form.cleaned_data['status']
            todo.content = form.cleaned_data['content']
            todo.save()
            return redirect(todo_view, pk=todo.pk)
        else:
            return render(request, 'edit.html', context={'form': form, 'todo': todo})


def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo': todo})
    elif request.method == 'POST':
        todo.delete()
        return redirect(index_view)
