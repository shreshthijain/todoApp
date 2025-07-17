from django.db import models

# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.text}'

class History(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='Anonymous')
    action = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.text}'