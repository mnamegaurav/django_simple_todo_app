from django.shortcuts import render, redirect
from .models  import ToDo
from .forms import ToDoForm

# Create your views here.

def index(request):

	form = ToDoForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			form = ToDoForm()
	
	todo_list = ToDo.objects.all().order_by('id')
	#print(type(todo_list))  #<class 'django.db.models.query.QuerySet'>

	context = {'todo_list': todo_list, 'form':form}
	
	return render(request, 'todo/index.html', context)

def deleteToDo(request, todo_id):
	todo = ToDo.objects.get(id=todo_id)
	if request.method == 'POST':
		todo.delete()
		form = ToDoForm()
		
	return redirect('index')