from django.urls import path
from .views import VacancyListView


app_name = 'vacancy'
urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy-list'),
]
