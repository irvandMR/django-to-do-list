from django.shortcuts import render, redirect
from .model import Task
from django.http import JsonResponse, HttpResponse

def index(request):
	if request.method == 'POST':
		title = request.POST.get('task')
		
		if title:
			Task.objects.create(title=title)
		return redirect('home')
	
	
	tasks = Task.objects.all()
	context = {'tasks': tasks}
	return render(request, 'todo/index.html', context)

def delete(request, id):
	task = Task.objects.get(id=id)
	task.delete()
	return redirect('home')

		
