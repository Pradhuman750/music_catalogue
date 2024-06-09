from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from music.models import Album, Artist, Playlist, Track


class PlaylistModelTestCase(TestCase):
    # Create test data: artist, album, track, and playlist
    def setUp(self):
        self.artist = Artist.objects.create(name="Artist Name")
        self.album = Album.objects.create(title="Album Title", artist=self.artist)
        self.track = Track.objects.create(title="Track Title", album=self.album)
        self.playlist = Playlist.objects.create(name="Test Playlist")

    def test_playlist_detail_view(self):
        # Test the playlist detail view
        response = self.client.get(
            reverse("playlist_detail", args=[self.playlist.uuid])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Playlist")

    def test_playlist_list_view(self):
        # Test the playlist list view
        response = self.client.get(reverse("playlist_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Playlist")

    @patch("music.views.inlineformset_factory")
    def test_playlist_create_view_success(self, mock_inlineformset_factory):
        # Test the playlist create view with successful
        form_data = {"name": "New Playlist"}
        mock_formset = mock_inlineformset_factory.return_value
        mock_formset.is_valid.return_value = True

        response = self.client.post(reverse("playlist_create"), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Playlist.objects.filter(name="New Playlist").exists())

    def test_playlist_create_view_failure(self):
        # Test the playlist create view with failed
        form_data = {"name": "New Playlist"}
        response = self.client.post(reverse("playlist_create"), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Playlist.objects.filter(name="New Playlist").exists())

    def test_playlist_update_view(self):
        # Test the playlist update view
        response = self.client.post(
            reverse("playlist_update", args=[self.playlist.uuid]),
            {"name": "Updated Playlist"},
        )
        self.assertEqual(response.status_code, 200)
        updated_playlist = Playlist.objects.get(id=self.playlist.id)
        self.assertEqual(updated_playlist.name, "Test Playlist")

    def test_playlist_delete_view(self):
        # Test the playlist delete view
        response = self.client.post(
            reverse("playlist_delete", args=[self.playlist.uuid])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Playlist.objects.filter(name="Test Playlist").exists())
