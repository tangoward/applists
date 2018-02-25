
from django.urls import path
from . import views


app_name = 'movies'


urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('create/', views.MovieCreate.as_view(), name='movie_create'),
    path('update/<int:pk>', views.MovieUpdate.as_view(), name='movie_update'),
    path('delete/<int:pk>', views.MovieDelete.as_view(), name='movie_delete'),
]
