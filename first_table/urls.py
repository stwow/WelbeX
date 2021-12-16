from .views import index, sorts
from django.urls import path

app_name = 'table'

urlpatterns = [
    path('', index, name='index'),
    path('sort/', sorts, name='sorts'),
]

