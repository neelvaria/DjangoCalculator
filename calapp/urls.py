from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.indexpage),
    path('submitquery',views.submitquery,name="submitquery")
]
