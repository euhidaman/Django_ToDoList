from django.contrib import admin
from django.urls import include, path
from ToDoList import views

urlpatterns = [
    path('', include('ToDoList.urls')),
    path('admin/', admin.site.urls),
]