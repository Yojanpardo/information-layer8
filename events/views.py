from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Event
from .forms import EventForm

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    success_url = reverse_lazy('events:event')
    fields = ['date_start', 'date_end', 'title',
              'description', 'location', 'timezone',
              'organizer', 'email']

class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    success_url = reverse_lazy('events:event')
    fields = ['date_start', 'date_end', 'title',
              'description', 'location', 'timezone',
              'organizer', 'email']

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events:event')
