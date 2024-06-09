from rest_framework import serializers

from .models import Album, Artist, Playlist, PlaylistTrack, Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Track
        fields = "__all__"


class PlaylistTrackSerializer(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = PlaylistTrack
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    playlist_tracks = PlaylistTrackSerializer(many=True)

    class Meta:
        model = Playlist
        fields = "__all__"
