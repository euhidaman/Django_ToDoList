# video time ==> 6:47:00

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'ToDoList/index.html')

@csrf_exempt
def add_todo(request):
    print(request.POST)
    return render(request, 'ToDoList/index.html')
