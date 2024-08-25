from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm, SearchForm

def todo_list(request):
    todos = Todo.objects.all()
    todo_form = TodoForm()
    search_form = SearchForm()

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save()
            return JsonResponse({
                'title': todo.title,
                'status': todo.status,
            })

    search_query = request.GET.get('search_query', '')
    if search_query:
        todos = todos.filter(title__icontains=search_query)

    context = {
        'todos': todos,
        'todo_form': todo_form,
        'search_form': search_form,
    }
    return render(request, 'todos/todo_list.html', context)
