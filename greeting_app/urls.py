from django.urls import path
from . import views

app_name = 'greeting_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('names/', views.name_list, name='name_list'),
]