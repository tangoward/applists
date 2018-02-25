from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie
# Create your views here.


class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movie_list.html'

    def get(self, request, *args, **kwargs):

        movie_name = request.GET.get('name', None)
        if movie_name:
            movies = self.model.objects.filter(name__icontains=movie_name)
        else:
            movies = self.model.objects.all()
        return render(request, self.template_name, {'movies': movies})


class MovieCreate(CreateView):
    model = Movie
    fields = ('name',)
    success_url = reverse_lazy('movies:movie_list')
    template_name = 'movies/create_movie.html'


class MovieUpdate(UpdateView):
    model = Movie
    fields = ('name',)
    success_url = reverse_lazy('movies:movie_list')
    template_name = 'movies/update_movie.html'


class MovieDelete(DeleteView):
    model = Movie
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('movies:movie_list')
