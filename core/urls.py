from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('geo.urls', namespace='geo')),
    path('api/', include('geo_api.urls', namespace='geo_api')),
]
