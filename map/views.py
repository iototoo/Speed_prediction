from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from io import StringIO
from urllib.parse import quote
from django.db import models
from .models import Map    
import itertools as it
from django.urls import reverse

import folium
import pandas as pd
import numpy as np
import geocoder
# from folium.plugins import MinMap
from folium import IFrame, Popup, plugins
from folium.plugins import MarkerCluster
# from scipy.spatial import ConvexHull
# from IPython.display import Javascript
from os.path import exists
from folium.utilities import deep_copy
# from shapely.geometry import Point, Polygon
import jinja2


# Create your views here.

# Map page
def index(request):
    return render(request, 'map/index.html')

# Detail page
def data_detail(request):
    return render(request, 'map/detail_list.html')

# Map Detail Date page
def detail_list(request, gpot_id):
    print(f'gpot_id:{gpot_id}')
    qst = Map.objects.all()
    qst = qst.filter(gpot_id = gpot_id )
    print(qst.count(), qst.query)
    # query = request.GET.get('q','')
    # if query:
    #     qst = Map.objects.filter(gpot_id__icontains=query)
    return render(request, 'map/detail_list.html', {'detail_list':qst})

# 행정동 선택을 위한 Query
def map_data(request, dong):
    print(dong)
    queryset = Map.objects.all()
    queryset = queryset.filter(dong = dong)
    # queryset.delete()
    print(queryset.count(), queryset.query)
    return queryset

## folium 
# DL_Speed값에 따라 색상을 결정
def wdl_speed_color(x):
    """
    dl_speed 값으로 색상코드를 반환
    - 파라미터 : dl_speed(숫자)
    - 반환값 : 색상값(문자열)
    """
    if x >= 1400:
        color = 'red'
    elif 1000 <= x < 1400:
        color = 'orange'
    elif 800 <= x < 1000:
        color = 'yellow'
    elif 600 <= x < 800:
        color = 'green'
    elif 300 <= x < 600:
        color = 'blue'
    else :
        color = 'black'
    return color


def folium_map(request, dong): 
    # locations = []
    qs = map_data(request, dong) 
    map = folium.Map(location=[qs[0].w_lat, qs[0].w_lon], 
    zoom_start=16.5,
    width='100%',
    height='100%')

    for d in qs:
        # df = pd.DataFrame(data = [[d.dong, d.gpot_id, d.pred_dl_speed, d.w_sinr]], columns=['행정동','gpot_id', '예측속도(DL)', 'W-SINR'])
        data = [['행정동', d.dong],['GPOT_ID', d.gpot_id], ['예측속도(DL)', d.pred_dl_speed], ['W-SINR', d.w_sinr] ]
        df = pd.DataFrame(data=data, columns=['구분', '내용'])
        rdf = df.iloc[1, 1]  #gpot_id 값 선택
        html = df.to_html(index=False, 
                        classes='table table-striped table-hover table-sm  table-responsive table-bordered table-borderless table-light  text-primary text-center')
        # 버튼 클릭스 gpot_id 기준으로 Table 생성 : map/detail_list.html
        html += "<button><a href='" + reverse("detail_list", kwargs={'gpot_id': rdf}) +"'>상세보기</a></button>"
        print(html)

        folium.Circle(
            location=[d.w_lat, d.w_lon], 
            popup = folium.Popup(html, max_width= 300),
            radius = 8,  #크기 지정
            color='black', #테두리 색상
            fill_color=wdl_speed_color(d.pred_dl_speed),
            fill_opacity=1.,
            weight=1).add_to(map)
    
    # 클릭 통해 지도 화면 확대
    plugins.ScrollZoomToggler().add_to(map)
    # 거리 측정 툴(자)
    plugins.MeasureControl().add_to(map)
    # 작은 지도 보여주기
    # plugins.MiniMap(zoom_level_offset=-5).add_to(fmap)

    fmap = map._repr_html_()
    context = {'fmap' : fmap}

    return render(request, '../templates/map/index.html', context)


# def chart_line(request):
#     gpot_id = 17796951
#     lables = []
#     data = []
#     queryset = Map.objects.order_by('day')[:10]
#     for i in queryset:
#         lables.append(i.day)
#         data.append(i.pred_dl_speed)
#         data.append(i.w_sinr)
#     return render(request, 'map/detail_list.html', {
#         'lables' : lables,
#         'data':data
#     })


