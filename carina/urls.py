from django.urls import path
from . import views

urlpatterns = [
    path('content/<str:code>/', views.get_content, name='get_content'),
]