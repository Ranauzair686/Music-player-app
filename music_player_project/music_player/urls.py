from django.urls import path
from . import views

app_name = 'music_player'

urlpatterns = [
    path('', views.upload_song, name='home'),  # Default URL pattern for the home page
    path('upload/', views.upload_song, name='upload_song'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
]
