from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('games/', views.game_list, name='game_list'),
    path('games/<int:pk>/', views.game_details, name='game_details'),
]
