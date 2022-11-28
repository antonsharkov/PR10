from django.urls import path
from . import views


urlpatterns = [
    path('<str:array>/<int:s1>/<int:s2>', views.index)
]