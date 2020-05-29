from django.db import models

STATUS_CHOICES = [('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')]


class Todo(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    date = models.DateField(null=False, blank=False, verbose_name='Дата выполнения')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name='Статус')
    content = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.description}, {self.status}, {self.content},'
