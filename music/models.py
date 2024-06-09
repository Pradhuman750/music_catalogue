import datetime
import uuid

from django.db import models


class Artist(models.Model):
    """
    Model for store Artist data.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    Model for store Album data.
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Track(models.Model):
    """
    Model for store Track data.
    """

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.DurationField(default=datetime.timedelta(minutes=0))

    def __str__(self):
        return self.title


class Playlist(models.Model):
    """
    Model for store Playlist data.
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PlaylistTrack(models.Model):
    """
    Model for store PlaylistTrack data.
    """

    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="playlist_tracks"
    )
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}: {self.track.title}"
