from django.urls import path
from . import views

urlpatterns = [
    path('zoo-entrance/', views.index, name='zoo_entrance'),
]
