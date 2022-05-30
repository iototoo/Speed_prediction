
from django.urls import URLPattern
# from django.conf.urls import url, include
from django.urls import path
from . import views

apps_name = 'map'

urlpatterns = [
    path('', views.index),
    path('map/', views.index, name="map"),
    path('detail/', views.data_detail, name='detail'),
    path('<gpot_id>/detail', views.detail_list, name="detail_list"),
    path('<str:dong>', views.folium_map, name="map-dong"),
    # path('chart/', views.chart, name='chart'),
    # path('chart_bar', views.chart_bar, name="chart_bar"),
]