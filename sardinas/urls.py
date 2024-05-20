from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("web/", include("web.urls")),
    path("admin/", admin.site.urls),
]