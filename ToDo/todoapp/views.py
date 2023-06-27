
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Mytodo
from .forms import TodoForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class TaskList(ListView):
    model = Mytodo
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Mytodo
    context_object_name = 'task'
    template_name = 'task_detail.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('alltodos')

def alltodos(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alltodos')
    return render(request, 'alltodo.html', {'tasks': tasks, 'form': form})

def deleteItem(request, pk):
    task = Mytodo.objects.get(id=pk)    
    task.delete()
    return redirect('alltodos')

def updateItem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance = todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')
    return render(request, 'updateItem.html', {'todo': todo, 'updateForm': updateForm})


















# def todo_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'todoapp/todo_list.html', {'tasks': tasks})

# def add_task(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         Task.objects.create(title=title)
#         return redirect('todo_list')
#     return render(request, 'todoapp/add_task.html')
