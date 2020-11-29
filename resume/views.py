from django.shortcuts import render

from django.views import View
from .models import Resume
from django.apps import apps


# Create your views here.

class ResumeListView(View):
    template_name = 'resume/resume_list.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['resume_list'] = Resume.objects.all()
        return render(request, self.template_name, context)
