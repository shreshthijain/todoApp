from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  
    path('add', views.add_todo_item, name='add_todo_item'),
    path('complete/<int:item_id>', views.complete_todo_item, name='complete_todo_item'),
    path('delete', views.delete_completed_item, name='delete_completed_item'),
    path('deleteAll', views.delete_all_items, name='delete_all_items'),
    path('history', views.history, name='history'),
    path('about', views.about, name='about'),
]
