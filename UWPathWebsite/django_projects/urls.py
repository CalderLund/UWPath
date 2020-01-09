"""django_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib import admin
import UWPath.views as uwPath

urlpatterns = [
    path('', uwPath.index, name='index'),
    path(r'admin/', admin.site.urls),
    path(r'api/', uwPath.AllApp.as_view()),
    path(r'api/course-info/get/<str:pk>', uwPath.Course_Info_API.as_view()),
    path(r'api/course-info/', uwPath.Course_Info_List.as_view()),
    path(r'api/prereqs/', uwPath.Prereqs_List.as_view()),
    path(r'api/prereqs/get/<str:pk>', uwPath.Prereqs_API.as_view()),
    path(r'api/coreqs/', uwPath.Coreqs_List.as_view()),
    path(r'api/coreqs/get/<str:pk>', uwPath.Coreqs_API.as_view()),
    path(r'api/antireqs/', uwPath.Antireqs_List.as_view()),
    path(r'api/antireqs/get/<str:pk>', uwPath.Antireqs_API.as_view()),
    path(r'api/requirements/', uwPath.Requirements_List.as_view()),
    path(r'api/requirements/get/<str:pk>', uwPath.Requirements_API.as_view()),
    path(r'api/communications/', uwPath.Communications_List.as_view()),
    path(r'api/communications/get/<int:pk>', uwPath.Communications_API.as_view()),

    #a little bit hardcoded below
    path(r'major/<str:major>/<str:majorExtended>/', uwPath.chosen_degree, name='chosen_degree'),
    path(r'major/<str:major>/', uwPath.chosen_degree, name='chosen_degree'),

    path(r'major/<str:major>/<str:majorExtended>/minor/<str:minor>/', uwPath.chosen_degree, name='chosen_degree'),
    path(r'major/<str:major>/<str:majorExtended>/minor/<str:minor>/<str:minorExtended>/', uwPath.chosen_degree, name='chosen_degree'),
    path(r'major/<str:major>/minor/<str:minor>/', uwPath.chosen_degree, name='chosen_degree'),
    path(r'major/<str:major>/minor/<str:minor>/<str:minorExtended>/', uwPath.chosen_degree, name='chosen_degree'),
    re_path(r'(?P<pk>\d+)', uwPath.AppView.as_view()),
]
