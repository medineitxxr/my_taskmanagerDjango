from django.db import models

# Create your models here.
class Task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle

