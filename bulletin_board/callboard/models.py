from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """Категории объявлений"""

    CHOICES = [
        ('Танки', 'Танки'),
        ('Хилы', 'Хилы'),
        ('ДД', 'ДД'),
        ('Торговцы', 'Торговцы'),
        ('Гилдмастеры', 'Гилдмастеры'),
        ('Квестгиверы', 'Квестгиверы'),
        ('Кузнецы', 'Кузнецы'),
        ('Кожевники', 'Кожевники'),
        ('Зельевары', 'Зельевары'),
        ('Мастера заклинаний', 'Мастера заклинаний'),
    ]
    name = models.CharField(max_length=255, choices=CHOICES, unique=True, )
    subscribers = models.ManyToManyField(User, null=True, blank=True, related_name='subscribers')

    def __str__(self):
        return f'{self.name}'


class Bulletin(models.Model):
    """Объявления"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField('Название', max_length=200)
    body = models.TextField('Текст', max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("bulletin-detail", kwargs={'pk': self.pk})


class Reply(models.Model):
    """Отклики на Объявления"""
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    bulletin = models.ForeignKey(Bulletin, related_name="replies", on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        return reverse("reply-create", kwargs={'pk': self.pk})
