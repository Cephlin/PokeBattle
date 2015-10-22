from django.http import HttpResponse
from django.template import RequestContext, loader

from player.models import Player
from pokemon.models import Pokemon


def index(request):
    players = Player.objects.all()
    pokemon = Pokemon.objects.all()
    template = loader.get_template('base.html')
    context = RequestContext(request, {
        'players_list': players,
        'pokemon_list': pokemon,
    })
    return HttpResponse(template.render(context))