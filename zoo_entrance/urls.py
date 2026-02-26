from django.urls import path
from . import views

app_name = 'zoo_entrance'

urlpatterns = [
    path('', views.index, name='index'),
    path("home/", views.zoo_home, name='zoo_home'),
    path("zoo_list/", views.zoo_list, name='zoo_list'),
]
