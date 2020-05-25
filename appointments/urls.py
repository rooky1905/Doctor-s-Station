from django.urls import path
from . import views

urlpatterns=[
    path('reception/',views.reception,name='reception'),
    path('updatepat/',views.updatepat,name='updatepat'),
    path('createpat/',views.createpat,name='crtpat'),
]