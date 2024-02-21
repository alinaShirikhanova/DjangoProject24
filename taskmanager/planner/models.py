from django.db import models

# Character - символ
# Field - поле
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
