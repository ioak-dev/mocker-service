from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('', views.get_update_domain),
    path('<str:id>', views.delete_domain),
    path('id/<str:id>', views.get_by_id)
]