from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    image = models.ImageField(
        upload_to='ads/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ads'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ads'
    )

    def __str__(self):
        return self.title

class Response(models.Model):

    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='responses'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField(
        'Сообщение'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'{self.author} -> {self.ad}'