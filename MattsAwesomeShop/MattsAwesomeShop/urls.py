from django.contrib import admin
from django.urls import path, include
from ToDoList.views import ToDoList


urlpatterns = [
    path('', include("ToDoList.urls")),
    path('admin/', admin.site.urls),
]
