# Register your models here.
from django.contrib import admin

from .models import Album, Artist, Playlist, PlaylistTrack, Track

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)


class PlaylistTrackInline(admin.TabularInline):
    model = PlaylistTrack
    extra = 1


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistTrackInline]
