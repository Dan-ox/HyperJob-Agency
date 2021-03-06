"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (
                    MainPageView,
                    HyperJobLoginView,
                    SignupView,
                    ProfileView,
                    VacancyCreateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main-page'),
    path('home/', ProfileView.as_view(), name='profile'),
    path('login', HyperJobLoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('vacancy/new', VacancyCreateView.as_view(), name='vacancy-create'),


    # app urls
    path('resumes/', include('resume.urls')),
    path('vacancies/', include('vacancy.urls')),
]
