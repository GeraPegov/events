from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/events/',
        views.EventView.as_view(),
        name='events'
    )
]