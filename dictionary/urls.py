from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('get_query/', views.get_query, name='query'),
    path('about/', views.about, name='about'),
    path('content/', views.content, name='content'),
    path('delete/<id>', views.delete, name='delete'),
]