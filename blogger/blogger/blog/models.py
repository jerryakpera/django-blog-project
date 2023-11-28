from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=10)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse(
            "post_single",
            args=[
                self.slug,
            ],
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-created_at",)
