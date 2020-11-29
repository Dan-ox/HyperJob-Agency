from django.shortcuts import render

from django.views import View
from .models import Vacancy, User


# Create your views here.

class VacancyListView(View):
    template_name = 'vacancy/vacancy_list.html'

    def get(self, request, *args, **kwargs):
        context = {'vacancy_list': Vacancy.objects.all()}
        return render(request, self.template_name, context)
