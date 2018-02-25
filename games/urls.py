
from django.urls import path
from . import views


app_name = 'games'

urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
    path('create/', views.GameCreate.as_view(), name='game_create'),
    path('update/<int:pk>', views.GameUpdate.as_view(), name='game_update'),
    path('delete/<int:pk>', views.GameDelete.as_view(), name='game_delete'),
]
