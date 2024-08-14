from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import ToDoList, ToDoItem
from django.views.generic import ListView

# Create your views here.

class ListListView(ListView):
    model = ToDoList
    template_name = "ToDoList/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "ToDoList/ToDoList.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context = super().get_context_data()
        context["ToDoList"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
