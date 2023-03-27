from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('members', views.create_team, name='members'),
    path('done', views.done, name='done')
]
