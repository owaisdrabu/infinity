from django.urls import path
from . import views


urlpatterns = [
    path('', views.stones, name='stones'),
]