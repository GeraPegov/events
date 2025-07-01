from django.shortcuts import render
from django.views.generic import ListView
from .forms import SearchNameForm
from events.models import Event


class EventView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        queryset = Event.objects.filter(status='open')

        name_param = self.request.GET.get('name')
        if name_param:
            queryset = queryset.filter(name__icontains=name_param)
        return queryset.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['form'] = SearchNameForm()
        return context

