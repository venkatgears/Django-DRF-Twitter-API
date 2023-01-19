from django.urls import path
from . import views


urlpatterns = [
    path("", views.endpoints),
    path("profiles/", views.profile_list),
    path("create_profile/<str:username>", views.add_profile),
    path("api/v1/<str:username>", views.crud_profile),
]
