from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
    path('admin-api/', index, name='admin-api'),
]
