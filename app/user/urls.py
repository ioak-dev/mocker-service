from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('', views.do),
    path('all', views.get_all),
    path('authorize_user', views.authorize_user),
    path('permittedActions', views.permittedActions)
]
