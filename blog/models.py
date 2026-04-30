from django.db import models
from django.utils import timezone

from authentication.models import User
from common.models import NameSlugDescriptionBaseModel


class Blog(NameSlugDescriptionBaseModel):
    title = models.CharField(max_length=255, verbose_name="Blog Title")
    content = models.TextField(verbose_name="Content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    tag = models.CharField(max_length=555, verbose_name="Blog Tag", null=True, blank=True)
    image = models.ImageField(upload_to="blog_images/", verbose_name="Blog Image", null=True, blank=True)
    image_caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="Image Caption")



    def __str__(self):
        return self.title


