from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('<str:project_reference>/domain/<str:domain_name>', views.domain_endpoint)
]