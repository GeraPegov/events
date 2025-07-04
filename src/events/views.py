from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from events.models import Event


class EventsView(APIView):

    def get(self, request):
        queryset = Event.objects.all().order_by('-date')
        if request.query_params:
            event_name = request.query_params.get('search_name')
            queryset = queryset.filter(Q(name__icontains=event_name))
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        results = [{
                'results': {
                    "Название мероприятия": event.name,
                    "Дата мероприятия": event.date,
                    "Место проведения": event.place.name
                    }
            } for event in page]
        
        return paginator.get_paginated_response(results)
