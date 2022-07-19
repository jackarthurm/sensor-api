from django.contrib import admin
from django.urls import (
    path,
    include,
    URLPattern,
)

urlpatterns: list[URLPattern] = [
    path('admin/', admin.site.urls),
    path("api/", include("sensor_api.urls")),
]
