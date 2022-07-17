from typing import List

from django.contrib import admin
from django.urls import (
    path,
    include,
    URLPattern,
)

urlpatterns: List[URLPattern] = [
    path('admin/', admin.site.urls),
    path("api/", include("sensor_api.urls")),
]
