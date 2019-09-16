from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length = 300)
    task_done = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f'{self.title}'