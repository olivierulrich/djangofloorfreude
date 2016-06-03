from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView

from events.models import Event


class EventList(ListView):
    model = Event
    template_name = 'eventList.html'
