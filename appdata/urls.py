from django.urls import path,include
from .views import dataListView,dataView
urlpatterns = [
    path('',dataListView.as_view(),name='data-list'),
    path('new',dataView.as_view(),name="data-make"),
]
