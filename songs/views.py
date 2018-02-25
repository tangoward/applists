
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Song
# Create your views here.


class SongListView(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'songs/song_list.html'

    def get(self, request, *args, **kwargs):
        song_name = request.GET.get('name')
        if song_name:
        	# Search using the name of the song or name of the artist
            songs = self.model.objects.filter(Q(name__icontains=song_name) | Q(artist_name__icontains=song_name)).distinct()
        else:
            songs = self.model.objects.all()
        return render(request, self.template_name, {'songs': songs})


class SongCreate(CreateView):
    model = Song
    fields = ('name', 'artist_name')
    success_url = reverse_lazy('songs:song_list')
    template_name = 'songs/create_song.html'


class SongUpdate(UpdateView):
    model = Song
    fields = ('name', 'artist_name')
    success_url = reverse_lazy('songs:song_list')
    template_name = 'songs/update_song.html'


class SongDelete(DeleteView):
    model = Song
    template_name = 'songs/delete_song.html'
    success_url = reverse_lazy('songs:song_list')
