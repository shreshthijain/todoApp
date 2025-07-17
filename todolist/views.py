from django.shortcuts import render, redirect
from .forms import TodoItemForm
from .models import History, TodoItem
from django.views.decorators.http import require_POST, require_GET

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
    
        # Log the action in History
        history_item = History(
            text=new_item.text,
            created_by=request.user.username if request.user.is_authenticated else 'Anonymous',
            action='Item Added'
        )
        history_item.save()
        return redirect('index')
    
def complete_todo_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = True
    item.save()
    # Log the action in History
    history_item = History(
        text=item.text,
        created_by=request.user.username if request.user.is_authenticated else 'Anonymous',
        action='Item Completed'
    )
    history_item.save()
    return redirect('index')

def delete_completed_item(request):
    item = TodoItem.objects.filter(completed=True)
    item.delete()
    history_item = History(
        created_by=request.user.username if request.user.is_authenticated else 'Anonymous',
        action='Item Deleted'
    )
    history_item.save()
    return redirect('index')

def delete_all_items(request):
    TodoItem.objects.all().delete()
    history_item = History(
        created_by=request.user.username if request.user.is_authenticated else 'Anonymous',
        action='All Items Deleted'
    )
    history_item.save()
    return redirect('index')

@require_GET
def history(request):
    history_items = History.objects.order_by('-created_at')
    context = {
        'history_items': history_items
    }
    return render(request, 'todolist/history.html', context)