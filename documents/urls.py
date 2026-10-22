from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path(
        "download/<int:document_id>/",
        views.download_document,
        name="download_document"
    ),
    path(
        "share/<int:document_id>/",
        views.share_document,
        name="share_document"
    ),
    path(
        "revoke/<int:document_id>/<int:user_id>/",
        views.revoke_access,
        name="revoke_access"
    ),
]