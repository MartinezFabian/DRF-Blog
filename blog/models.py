from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL  # reference to users/CustomUser


def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    # filter by default the posts with status 'Published'.
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="P")

    STATUS_CHOICES = (
        ("D", "Draft"),
        ("P", "Published"),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")
    image = models.ImageField(upload_to=upload_to, default="posts/default.png")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    objects = models.Manager()  # default manager
    published_objects = PostObjects()  # custom manager PostObjects

    class Meta:
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs):
        # Generar el slug automáticamente a partir del título
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
