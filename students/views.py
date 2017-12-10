from django.views.generic import ListView
from .models import Incident


class IncidentList(ListView):
    model = Incident
    ordering = ['-status', '-date_occurred', 'student', ]
