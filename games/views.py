from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Games
from .serializers import GameSerializer


@api_view(['GET', 'POST'])
def game_list(request):
    """
    returns/adds list of games
    """
    if request.method == 'GET':
        games = Games.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)

    elif request.method == 'POST':
        game_serializer = GameSerializer(data=request.data)

        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
        return Response(game_serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST'])
def game_details(request, pk):
    """
    returns/ adds/ updates a single game using API
    """
    try:
        game = Games.objects.get(pk=pk)
    except Games.DoesNotExist:
        # return JSONResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)

    if request.method == 'PUT':
        game_serializer = GameSerializer(game, data=request.data)

        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
