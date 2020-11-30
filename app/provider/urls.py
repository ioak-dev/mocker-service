from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('<str:project_reference>/domain/<str:domain_name>', views.get_domain),
    path('<str:project_reference>/domain/<str:domain_name>/<str:id>', views.get_domain_by_id),
    
    path('<str:project_reference>/custom/<str:endpoint_name>', views.actions_for_custom_endpoint)
]