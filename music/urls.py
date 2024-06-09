from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    AlbumViewSet,
    ArtistViewSet,
    PlaylistViewSet,
    TrackViewSet,
    playlist_create,
    playlist_delete,
    playlist_detail,
    playlist_list,
    playlist_update,
)

# from .views import playlist_list, playlist_detail
router = DefaultRouter()
router.register(r"artists", ArtistViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"tracks", TrackViewSet)
router.register(r"playlistsAPI", PlaylistViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("playlists/", playlist_list, name="playlist_list"),
    path("playlists/<uuid:uuid>/", playlist_detail, name="playlist_detail"),
    path("playlists/create/", playlist_create, name="playlist_create"),
    path("playlists/<uuid:uuid>/update/", playlist_update, name="playlist_update"),
    path("playlists/<uuid:uuid>/delete/", playlist_delete, name="playlist_delete"),
]
