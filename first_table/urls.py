from .views import index
from django.urls import path, include

app_name = 'tables'

urlpatterns = [
    path('', index, name='index'),
]

