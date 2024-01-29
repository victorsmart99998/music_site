from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200, null=True)
    audio_file = models.FileField(upload_to='uploads/')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
