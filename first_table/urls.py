from .views import index, sort_table
from django.urls import path, include

app_name = 'tables'

urlpatterns = [
    path('', index, name='index'),
    path('sort/', sort_table, name = 'sort_table')
]

