from django.urls import path
from django.views.generic import TemplateView

app_name = 'geo'

urlpatterns = [
    path('', TemplateView.as_view(template_name="geo/index.html")),
]
