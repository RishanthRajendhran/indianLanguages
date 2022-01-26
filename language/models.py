from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)
    nameInNativeScript = models.CharField(max_length=20)
    greetingInNativeScript = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name