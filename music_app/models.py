from django.db import models
from userauths.models import User


# Create your models here.

RATING = (
    ('Draft', 'Draft'),
    ('Disabled', 'Disabled'),
    ('Rejected', 'Rejected'),
    ('In_review', 'In_review'),
    ('Published', 'Published'),
)

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

class SongReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "song review"
