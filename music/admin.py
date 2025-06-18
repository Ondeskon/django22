from django.contrib import admin
from .models import Artist, Album, Song, Message

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'birth_date')
    search_fields = ('name', 'country')
    list_filter = ('country',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__name')
    list_filter = ('release_date', 'artist')
    date_hierarchy = 'release_date'

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'track_number', 'duration')
    search_fields = ('title', 'album__title', 'album__artist__name')
    list_filter = ('album__artist', 'album')
    ordering = ('album', 'track_number')

admin.site.register(Message)
