from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from django.views.generic import TemplateView
from events.forms import SearchNameForm
from django.contrib.auth.mixins import LoginRequiredMixin


class EventsTemplatesView(LoginRequiredMixin, TemplateView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    template_name = 'events/events.html'
    login_url = '/auth/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchNameForm()
        # Получаем параметр 'name' из GET-запроса
        search_query = self.request.GET.get('name', '')
        
        # Фильтруем мероприятия
        events = Event.objects.filter(status="open")
        if search_query:
            events = events.filter(name__icontains=search_query)  # Регистронезависимый поиск
        context['events'] = events
        context['form'] = form
        context['search_query'] = search_query  # Чтобы сохранить введённый текст в форме
        return context