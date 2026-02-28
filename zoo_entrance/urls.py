from django.urls import path
from . import views

app_name = 'zoo_entrance'

urlpatterns = [
    path('', views.index, name='index'),
    path("home/", views.zoo_home, name='zoo_home'),
    path('zoo/<int:pk>/', views.zoo_detail, name='zoo_detail'),
    #path("zoo_list/", views.zoo_list, name='zoo_list'), # commented out because we are rendering zoo list in home.html now
]
