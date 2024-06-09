from django import forms

from .models import Playlist, PlaylistTrack


class PlaylistForm(forms.ModelForm):
    """
    Form for creating or updating a playlist.
    """

    class Meta:
        model = Playlist
        fields = ["name"]


class PlaylistTrackForm(forms.ModelForm):
    """
    Form for adding or updating tracks in a playlist.
    """

    class Meta:
        model = PlaylistTrack
        fields = ["track", "order"]
