from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.TextField(verbose_name='Описание',max_length=200, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', max_length=10, null=False, blank=False, default="new")
    deadline = models.TextField(verbose_name='Дата выполнения', max_length=16, null=False, blank=False, default="")
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"