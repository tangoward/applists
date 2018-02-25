
from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
    path('', views.SongListView.as_view(), name='song_list'),
    path('create/', views.SongCreate.as_view(), name='song_create'),
    path('update/<int:pk>', views.SongUpdate.as_view(), name='song_update'),
    path('delete/<int:pk>', views.SongDelete.as_view(), name='song_delete'),
]
