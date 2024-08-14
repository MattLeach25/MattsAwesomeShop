from django.contrib import admin
from django.urls import path
from ToDoList.views import ToDoList


urlpatterns = [
    path('', ToDoList, name='ToDoList'),
    path('admin/', admin.site.urls),
]
