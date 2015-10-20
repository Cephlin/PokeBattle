from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Player


def index(request):
    players = Player.objects.all()
    template = loader.get_template('base.html')
    context = RequestContext(request, {
        'player_list': players,
    })
    return HttpResponse(template.render(context))