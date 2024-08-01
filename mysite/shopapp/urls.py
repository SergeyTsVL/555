from django.urls import path
from . import views

urlpatterns = [
    path('platform/', views.index, name='index'),
    path('platform/gemes/', views.index2, name='index2'),
    path('platform/cart/', views.index3, name='index3'),
]

