from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genre/<int:pk>/', views.GenreRetriveUpdateDestroyView.as_view(), name='genre_detail_view'),
]