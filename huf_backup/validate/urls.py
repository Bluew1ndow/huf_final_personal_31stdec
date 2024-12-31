from django.urls import path
from . import views

urlpatterns = [
    path("fetchlinks",views.fetchlinks,name='fetchlinks'),
    path("checkresponse",views.checkresponse,name='validate'),
    path("checkoccurrence",views.checkoccurrence,name='checkoccurrence')
]
