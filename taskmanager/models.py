from django.db import models


# Create your models here.
class Todo(models.Model):
    #title, decription, completed 
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
    #save this as a title 
    def __str__(self) -> str:
        return self.title
    
