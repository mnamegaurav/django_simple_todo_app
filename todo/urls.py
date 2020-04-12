from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('deleteToDo',views.deleteToDo,name="deleteToDo")
]
