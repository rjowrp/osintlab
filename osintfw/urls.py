from django.urls import path
from . import views

urlpatterns = [
    path('chartfw',views.chartfw, name="osintfw"),
    # path('searchDatabase',views.searchDatabase, name="searchDatabase"),
]

