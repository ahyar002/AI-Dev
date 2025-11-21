from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    ordering = ['-created_at']

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'due_date']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'due_date', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

from django.http import JsonResponse

def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
        
    return redirect('todo_list')
