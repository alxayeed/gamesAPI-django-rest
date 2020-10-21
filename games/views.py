from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Games
from .serializers import GameSerializer
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'appliation/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def game_list(request):
    """
    returns/adds list of games
    """
    if request.method == 'GET':
        games = Games.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return JSONResponse(games_serializer.data)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)

        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(game_serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def game_details(request, pk):
    """
    returns/ adds/ updates a single game using API
    """
    try:
        game = Games.objects.get(pk=pk)
    except Games.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JSONResponse(game_serializer.data)

    if request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=game_data)

        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(game_serializer.data)
        return JSONResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        game.delete()
        return JSONResponse(status=status.HTTP_204_NO_CONTENT)
