from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    def __str__(self) -> str:
        return self.title

    # filtrar de manera predeterminada los post con estado 'Published'
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="P")

    class Meta:
        ordering = ["-published"]

    STATUS_CHOICES = (
        ("D", "Draft"),
        ("P", "Published"),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
