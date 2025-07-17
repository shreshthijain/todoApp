from django.shortcuts import render, redirect
from .forms import TodoItemForm
from .models import TodoItem
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = TodoItem.objects.order_by('id')
    form = TodoItemForm()

    context = {
        'todo_items': todo_items,
        'form': form
    }
    return render(request, 'todolist/index.html', context)

@require_POST
def add_todo_item(request):
    # if not request.POST:
    form = TodoItemForm(request.POST)
    if form.is_valid():
        new_item = TodoItem(text=request.POST['text'])
        new_item.save()
        return redirect('index')
    
def complete_todo_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('index')

def delete_completed_item(request):
    item = TodoItem.objects.filter(completed=True)
    item.delete()
    return redirect('index')

def delete_all_items(request):
    TodoItem.objects.all().delete()
    return redirect('index')
        
    