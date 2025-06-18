import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hiphop.settings')
django.setup()

from music.models import Artist, Album, Song

# Create artists
artists = [
    {
        'name': 'Eminem',
        'bio': 'Marshall Bruce Mathers III, známý jako Eminem, je americký rapper, textař a producent.',
        'birth_date': datetime(1972, 10, 17),
        'country': 'USA'
    },
    {
        'name': 'Kendrick Lamar',
        'bio': 'Kendrick Lamar Duckworth je americký rapper a textař z Comptonu v Kalifornii.',
        'birth_date': datetime(1987, 6, 17),
        'country': 'USA'
    },
    {
        'name': 'Tupac Shakur',
        'bio': 'Tupac Amaru Shakur byl americký rapper, herec a aktivista.',
        'birth_date': datetime(1971, 6, 16),
        'country': 'USA'
    }
]

# Create albums
albums = [
    {
        'title': 'The Marshall Mathers LP',
        'release_date': datetime(2000, 5, 23),
        'description': 'Třetí studiové album amerického rappera Eminema.'
    },
    {
        'title': 'To Pimp a Butterfly',
        'release_date': datetime(2015, 3, 15),
        'description': 'Třetí studiové album amerického rappera Kendricka Lamara.'
    },
    {
        'title': 'All Eyez on Me',
        'release_date': datetime(1996, 2, 13),
        'description': 'Čtvrté a poslední studiové album amerického rappera Tupaca Shakura.'
    }
]

# Create songs
songs = [
    {
        'title': 'The Real Slim Shady',
        'duration': timedelta(minutes=4, seconds=44),
        'track_number': 1,
        'lyrics': 'May I have your attention, please?'
    },
    {
        'title': 'King Kunta',
        'duration': timedelta(minutes=3, seconds=54),
        'track_number': 1,
        'lyrics': 'I got a bone to pick'
    },
    {
        'title': 'California Love',
        'duration': timedelta(minutes=4, seconds=45),
        'track_number': 1,
        'lyrics': 'California knows how to party'
    }
]

# Add data to database
for artist_data in artists:
    artist = Artist.objects.create(**artist_data)
    print(f"Created artist: {artist.name}")

for i, album_data in enumerate(albums):
    album = Album.objects.create(
        artist=Artist.objects.get(name=artists[i]['name']),
        **album_data
    )
    print(f"Created album: {album.title}")

for i, song_data in enumerate(songs):
    song = Song.objects.create(
        album=Album.objects.get(title=albums[i]['title']),
        **song_data
    )
    print(f"Created song: {song.title}")

print("Sample data created successfully!") 