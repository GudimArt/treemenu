from django.urls import path
from core.apps.treemenu.views import index


urlpatterns = [
    path("", index, name="index"),
]
