from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>', views.MovieRetriveUpdateDestroyView.as_view(), name='movie_detail_view'),
]