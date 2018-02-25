from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Game

# Create your views here.


class GameListView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'

    def get(self, request, *args, **kwargs):
        game_name = request.GET.get('name')
        if game_name:
            #Search using the name of the game or the developer
            games = self.model.objects.filter(Q(name__icontains=game_name) | Q(developer__icontains=game_name)).distinct()
        else:
            games = self.model.objects.all()
        return render(request, self.template_name, {'games': games})


class GameCreate(CreateView):
    model = Game
    fields = ('name', 'developer')
    success_url = reverse_lazy('games:game_list')
    template_name = 'games/create_game.html'


class GameUpdate(UpdateView):
    model = Game
    fields = ('name', 'developer')
    success_url = reverse_lazy('games:game_list')
    template_name = 'games/update_game.html'


class GameDelete(DeleteView):
    model = Game
    template_name = 'games/delete_game.html'
    success_url = reverse_lazy('games:game_list')
