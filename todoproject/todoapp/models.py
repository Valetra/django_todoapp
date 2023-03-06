from django.db import models
from django.contrib.auth.models import User

class TodoListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField() 
    done = models.BooleanField(default = False)

    def __str__(self):
        return f'Content: {self.content} | User: {self.user}'