from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Artist, Message

def home(request):
    return render(request, 'music/home.html')

def genres(request):
    genres_list = [
        {
            'name': 'Old School',
            'subgenres': ['Classic Hip Hop', 'Golden Age Hip Hop', 'Electro']
        },
        {
            'name': 'Boom Bap',
            'subgenres': ['Jazz Rap', 'Conscious Hip Hop', 'Underground Hip Hop']
        },
        {
            'name': 'Trap',
            'subgenres': ['Drill', 'Cloud Rap', 'Mumble Rap', 'Emo Rap']
        },
        {
            'name': 'G-Funk',
            'subgenres': ['West Coast Hip Hop', 'Gangsta Rap', 'Funk Rap']
        },
        {
            'name': 'Conscious Hip Hop',
            'subgenres': ['Political Hip Hop', 'Spiritual Hip Hop', 'Alternative Hip Hop']
        },
        {
            'name': 'Alternative Hip Hop',
            'subgenres': ['Experimental Hip Hop', 'Art Rap', 'Progressive Hip Hop']
        },
        {
            'name': 'Drill',
            'subgenres': ['UK Drill', 'Chicago Drill', 'Brooklyn Drill']
        },
        {
            'name': 'Lo-fi Hip Hop',
            'subgenres': ['Chillhop', 'Jazz Hop', 'Ambient Hip Hop']
        },
        {
            'name': 'Jazz Rap',
            'subgenres': ['Acid Jazz', 'Jazz Hop', 'Fusion Hip Hop']
        },
        {
            'name': 'East Coast',
            'subgenres': ['New York Hip Hop', 'Hardcore Hip Hop', 'Boom Bap']
        },
        {
            'name': 'West Coast',
            'subgenres': ['G-Funk', 'Gangsta Rap', 'Hyphy']
        },
        {
            'name': 'Dirty South',
            'subgenres': ['Crunk', 'Snap Music', 'Bounce Music']
        },
        {
            'name': 'UK Hip Hop',
            'subgenres': ['Grime', 'UK Drill', 'British Hip Hop']
        },
        {
            'name': 'French Hip Hop',
            'subgenres': ['French Rap', 'French Drill', 'French Trap']
        },
        {
            'name': 'Korean Hip Hop',
            'subgenres': ['K-Hip Hop', 'Korean Trap', 'Korean R&B']
        }
    ]
    return render(request, 'music/genres.html', {'genres': genres_list})

def history(request):
    return render(request, 'music/history.html')

def artists(request):
    artists = Artist.objects.all()
    return render(request, 'music/artists.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'music/artist_detail.html', {'artist': artist})

def form(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            Message.objects.create(name=name, email=email, message=message)
            success = True
    return render(request, 'music/form.html', {'success': success})

def add_artist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth_date')
        country = request.POST.get('country')
        
        if name:
            artist = Artist.objects.create(
                name=name,
                bio=bio,
                birth_date=birth_date if birth_date else None,
                country=country
            )
            messages.success(request, f'Umělec {name} byl úspěšně přidán!')
            return redirect('artists')
    
    return render(request, 'music/add_artist.html')

def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        artist_name = artist.name
        artist.delete()
        messages.success(request, f'Umělec {artist_name} byl úspěšně smazán!')
        return redirect('artists')
    
    return render(request, 'music/delete_artist.html', {'artist': artist})
