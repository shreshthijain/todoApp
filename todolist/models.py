from django.db import models

# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=200, unique=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.text}'
    