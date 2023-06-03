from django.db import models

class TodoItem(models.Model):
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
