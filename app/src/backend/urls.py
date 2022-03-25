from django.urls import path

from .views import backend

app_name = 'backend'
urlpatterns = [
    path('', backend.index, name="index"),
]