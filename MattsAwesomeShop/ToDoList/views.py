from django.shortcuts import render

# Create your views here.

def ToDoList(request):
    return render(request, 'ToDoList/ToDoList.html')