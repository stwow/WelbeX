from .views import main
from django.urls import path

app_name = 'annot'

urlpatterns = [
    path('<int:pk>/', main, name='main'),
]

