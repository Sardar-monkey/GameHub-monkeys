import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from pytils.translit import slugify

class GameCategory(models.Model):
    gamename = models.CharField("Game name", max_length=100)
    gameimage = models.ImageField(upload_to='uploads/')
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return self.gamename
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.gamename)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.gameimage:
            if os.path.isfile(self.gameimage.path):
                os.remove(self.gameimage.path)
        super().delete(*args, **kwargs)


class GuideDesc(models.Model):
    title = models.CharField(max_length=120, verbose_name="Title")
    date = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='images/', verbose_name="Image")
    description = models.TextField(verbose_name="Description")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, verbose_name="category")

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
                
        super().delete(*args, **kwargs)
    