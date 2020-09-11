from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('<str:domainId>', views.get_fields_domainId)
]