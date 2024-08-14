from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7) # This allows me to use the function in another class to get the date 7 days from now.

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self): #This returns the URL dynamically instead of hard coding??
        return reverse("list", args=[self.id])

    def __str__(self): #what does self do?
        return self.title
    
class ToDoItem(models.Model): #What does models.Model do? Inheritance from models class gives me the properties I need.
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # Cascade means that all references to this item will be deleted when item is deleted.
    #models.ForeignKey refers to object in a database with many-to-one relationship instead of one-to-one.

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    
    class Meta: ordering = ["due_date"]