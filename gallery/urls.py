from django.urls import path
from . import views

urlpatterns = [
    path("preview/", views.gallery_preview, name="gallery-preview"),
    path("preview/<int:index>/", views.gallery_index, name="gallery-index"),
]
