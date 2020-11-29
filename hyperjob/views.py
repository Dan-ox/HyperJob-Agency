from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .forms import ResumeForm
from .forms import VacancyForm


# Create your views here.
class MainPageView(View):
    template_name = 'resume/main_page.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class HyperJobLoginView(LoginView):
    redirect_authenticated_user = False
    template_name = 'resume/login.html'


class ProfileView(View):
    template_name = 'resume/profile.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class VacancyCreateView(View):
    template_name = 'vacancy/vacancy_create.html'

    def get(self, request, *args, **kwargs):
        form = VacancyForm()
        context = {'form': form}
        return render(request, self.template_name, context)

