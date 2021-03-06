"""dclj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views as tokenViews

from swapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'reports', views.ReportViewSet)
router.register(r'activities', views.ActivityViewSet)


urlpatterns = [
    url(r'^users/create/', views.UserCreate.as_view()),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
#    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', tokenViews.obtain_auth_token),
]
