from django.db import models
from django.utils import timezone
# Create your models here.


class TodoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content








