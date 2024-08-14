from django.contrib import admin
from django.urls import path, include
from .views import PcCreateListView, PcRetrieveUpdateDestroyView, PcSsdCountView

urlpatterns = [
    path('pc/', PcCreateListView.as_view(), name='Pc-crate-list'),
    path('pc/<str:pk>/', PcRetrieveUpdateDestroyView.as_view(), name="Pc-dateil-views"),
    path('pcs/ssd_count/', PcSsdCountView.as_view(), name='pc-ssd-count'),
]
