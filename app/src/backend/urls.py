from django.urls import path

from .views import backend

app_name = 'backend'
urlpatterns = [
    path('', backend.IndexView.as_view(), name = 'index'),
    path('detail/<int:pk>/', backend.TermDetail.as_view(), name='detail')
]