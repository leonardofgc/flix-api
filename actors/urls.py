from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actor/<int:pk>/', views.ActorRetriveUpdateDestroyView.as_view(), name='actor_detail_view'),
]