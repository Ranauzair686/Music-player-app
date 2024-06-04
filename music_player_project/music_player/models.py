from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.title
