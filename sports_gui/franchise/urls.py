from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('league/', views.league, name = 'league'),
    path('date/', views.date, name = 'date'),
    path('season/', views.season, name = 'season'),
    path('league_query/',views.league_query, name='league_query'),
    path('team_query/',views.team_query, name='team_query'),
    path('game_query/',views.game_query, name='game_query'),
    path('ratings_query/',views.ratings_query, name='ratings_query'),
    path('season_query/',views.season_query, name='season_query'),
    path('results/',views.results, name='results'),
    path('move_teams/',views.move_teams, name='move_teams'),
    path('teamEntry/', views.teamEntry, name = 'teamEntry'),
    path('resultsEntered/', views.resultsEntered, name = 'resultsEntered'),
    path('leagueResult', views.leagueResult, name = 'leagueResult'),
    path('manual_insert_teams/',views.manual_insert_teams, name='manual_insert_teams')
]