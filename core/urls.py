"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from coreapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user-view')
router.register(r'sessions', views.SessionViewSet, base_name='session-view')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^me/', views.SelfView.as_view()),
    url(r'^mysession/', views.MySessionView.as_view()),
    url(r'^accounts/', include('rest_framework.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
]
