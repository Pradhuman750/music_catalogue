from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets

from .forms import PlaylistForm, PlaylistTrackForm
from .models import Album, Artist, Playlist, PlaylistTrack, Track
from .serializers import (
    AlbumSerializer,
    ArtistSerializer,
    PlaylistSerializer,
    TrackSerializer,
)


class ArtistViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Artist model.
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Album model.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Track model.
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Playlist model.
    """

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


def playlist_list(request):
    """
    View function to display a list of playlists.
    """
    playlists = Playlist.objects.all()
    return render(request, "catalogue/playlist_list.html", {"playlists": playlists})


def playlist_detail(request, uuid):
    """
    View function to display a detail of playlists.
    """
    playlist = get_object_or_404(Playlist, uuid=uuid)
    return render(request, "catalogue/playlist_detail.html", {"playlist": playlist})


def playlist_create(request):
    """
    View function to create a playlists.
    """
    PlaylistTrackFormSet = inlineformset_factory(
        Playlist, PlaylistTrack, form=PlaylistTrackForm, extra=1, can_delete=True
    )
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        formset = PlaylistTrackFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            playlist = form.save()
            formset.instance = playlist
            formset.save()
            return redirect("playlist_list")
    else:
        form = PlaylistForm()
        formset = PlaylistTrackFormSet()
    return render(
        request, "catalogue/playlist_form.html", {"form": form, "formset": formset}
    )


def playlist_update(request, uuid):
    """
    View function to update a playlists.
    """
    playlist = get_object_or_404(Playlist, uuid=uuid)
    PlaylistTrackFormSet = inlineformset_factory(
        Playlist, PlaylistTrack, form=PlaylistTrackForm, extra=1, can_delete=True
    )
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        formset = PlaylistTrackFormSet(request.POST, instance=playlist)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("playlist_detail", uuid=playlist.uuid)
    else:
        form = PlaylistForm(instance=playlist)
        formset = PlaylistTrackFormSet(instance=playlist)
    return render(
        request, "catalogue/playlist_form.html", {"form": form, "formset": formset}
    )


def playlist_delete(request, uuid):
    """
    View function to delete a playlists.
    """
    playlist = get_object_or_404(Playlist, uuid=uuid)
    if request.method == "POST":
        playlist.delete()
        return redirect("playlist_list")
    return render(
        request, "catalogue/playlist_confirm_delete.html", {"playlist": playlist}
    )
