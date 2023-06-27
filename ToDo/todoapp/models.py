# todo/models.py

from django.db import models

class Mytodo(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.task
