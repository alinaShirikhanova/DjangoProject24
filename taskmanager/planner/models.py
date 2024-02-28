from django.db import models

# Character - символ
# Field - поле
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

