from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('zanry/', views.genres, name='genres'),
    path('historie/', views.history, name='history'),
    path('umelci/', views.artists, name='artists'),
    path('umelci/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('umelci/pridat/', views.add_artist, name='add_artist'),
    path('umelci/<int:artist_id>/smazat/', views.delete_artist, name='delete_artist'),
    path('formular/', views.form, name='form'),
] 