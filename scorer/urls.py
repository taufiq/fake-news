from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('leaderboards', views.leaderboards, name='leaderboards'),
    path('result',
         views.result, name='checkArticle'),
]
