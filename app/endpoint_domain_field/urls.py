from django.urls import path

from . import views

urlpatterns =[
    path('<str:domain_id>', views.get_fields_domain_id)
]