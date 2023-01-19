from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("handler.urls")),
    path("admin/", admin.site.urls),
]
