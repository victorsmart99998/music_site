from django.db import models


# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200, null=True)
    audio_file = models.FileField(upload_to='uploads/')
    image = models.ImageField(null=True, blank=True)
    download_count = models.IntegerField(default=0, blank=True)
    play_count = models.IntegerField(default=0, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name
