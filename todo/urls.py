from django.urls import path
from todo.views import home, add_todo, edit_todo, delete_todo

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_todo, name='add_todo'),
    path('<int:todo_id>/edit/', edit_todo, name="edit_todo"),
    path('<int:todo_id>/delete/', delete_todo, name="delete_todo"),
]
