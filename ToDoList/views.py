from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from ToDoList.models import ToDo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'ToDoList/index.html', {"todo_items": todo_items})

# pathway, or flow ==>
# goes from submit in form(index.html) --> urls.py --> add_todo(request) function
@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = ToDo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect('/')

# pathway, or flow ==>
# goes from delete in form(index.html) --> urls.py --> delete_todo(request, todo_id) function
# here todo_id, is the id of the field in the database to be deleted, as passed from the index.html form
@csrf_exempt
def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
