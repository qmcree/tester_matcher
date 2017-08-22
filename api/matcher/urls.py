from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^options', views.list_options),
    url(r'^testers', views.list_testers),
]
