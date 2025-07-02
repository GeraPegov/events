from django.urls import path

from . import views

urlpatterns = [
    path(
        "events/",
        views.EventsTemplatesView.as_view(),
        name="events"
    )
    ]
