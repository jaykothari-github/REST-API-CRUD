from django.db import models

# Create your models here.

class TODO(models.Model):

    task = models.CharField(max_length=50)
    details = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task