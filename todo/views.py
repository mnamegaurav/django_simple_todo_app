from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models  import ToDo
from todo.forms import ToDoForm

# Create your views here.

def home(request):
	form = ToDoForm()
	todo_list = ToDo.objects.all()
	context = {'todo_list': todo_list, 'form':form}
	return render(request, 'todo/index.html', context)

def add_todo(request):
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data.get('text')
			new_todo = ToDo.objects.create(text=text)
			form = ToDoForm()
		
		todo_list = ToDo.objects.all()
		context = {'todo_list': todo_list, 'form':form}
		return render(request, 'todo/index.html', context)
	else:
		return redirect('home')


"""Edit view needs some work"""
def edit_todo(request, todo_id):
	todo = ToDo.objects.get(pk=todo_id)
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data.get('text')
			todo.text = text
			todo.save()
			form = ToDoForm()
		
		todo_list = ToDo.objects.all()
		context = {'todo_list': todo_list, 'form':form}
		return render(request, 'todo/index.html', context)
	else:
		form = ToDoForm(initial={'text':todo.text})
		context = {'form':form, 'todo': todo}
		return render(request, 'todo/edit.html', context)


def delete_todo(request, todo_id):
	if request.method == 'POST':
		todo = ToDo.objects.get(pk=todo_id)
		todo.delete()
	return redirect('home')	