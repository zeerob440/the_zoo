from django.urls import path
from . import views

app_name = 'zoo_entrance'

urlpatterns = [
    path('', views.index, name='index'),
    path("home/", views.zoo_home, name='zoo_home'),
    path('zoo/<int:pk>/', views.zoo_detail, name='zoo_detail'),
    path('zoo/new/', views.zoo_new, name='zoo_new'),
    path('zoo/<int:pk>/edit/', views.zoo_edit, name='zoo_edit'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/new/<int:pk>', views.animal_new, name='animal_new'),
    path('animal/<int:pk>/edit/', views.animal_edit, name='animal_edit'),
]

"""
    

    
"""