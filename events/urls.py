from django.conf.urls import url
from django.views.generic import TemplateView

from events.views import EventList
from . import views

urlpatterns = [
    url(r'^$', EventList.as_view(), name='eventList'),
]