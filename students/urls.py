# urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IncidentList

urlpatterns = [
    path('incidents/', login_required(IncidentList.as_view()),
         name='incident-list'),
]
