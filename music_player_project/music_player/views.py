from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_player:upload_song')
    else:
        form = SongForm()
    songs = Song.objects.all()
    return render(request, 'music_player/upload_song.html', {'form': form, 'songs': songs})

def play_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'music_player/play_song.html', {'song': song})
