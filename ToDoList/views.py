# video time ==> 6:47:00

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from ToDoList.models import ToDo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'ToDoList/index.html', {"todo_items": todo_items})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = ToDo.objects.create(added_date=current_date, text=content)
    length_of_todos = ToDo.objects.all().count()
    return HttpResponseRedirect('/ToDoList/')
