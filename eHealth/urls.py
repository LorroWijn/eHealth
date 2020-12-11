"""eHealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('mainpage/', include('mainpage.urls')),
    path('agenda/', include('agenda.urls')),
    path('contact_delta/', include('contact_delta.urls')),
    path('login/', include('login.urls')),
    path('nieuws/', include('nieuws.urls')),
    path('samenwerking/', include('samenwerking.urls')),
    path('webtest/', include('web_test.urls')),
    path('vitaliteit/', include('vitaliteit.urls')),
    path('vitaliteit/verbetering/', include('vitaliteit_verbetering.urls')),
    path('vitaliteit/applicaties/', include('vitaliteit_applicaties.urls')),
    path('vitaliteit/grip_op_coronastress/', include('vitaliteit_grip_op_coronastress.urls')),
    path('vitaliteit/psyfitter/', include('vitaliteit_psyfitter.urls')),
    path('vitaliteit/energyplatform/', include('vitaliteit_energyplatform.urls')),
    path('vitaliteit/proudwoman/', include('vitaliteit_proudwoman.urls')),
    path('vitaliteit/vgz_mindfulness_coach_app/', include('vitaliteit_vgz_mindfulness_coach_app.urls')),
    path('vitaliteit/fitstap/', include('vitaliteit_fitstap.urls')),
    path('admin/', admin.site.urls),
]
