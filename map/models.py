from django.db import models
from django.forms import IntegerField, DateField, FloatField
from django.urls import reverse

# Create your models here.

class Map(models.Model):
    index = models.IntegerField(primary_key=True)
    day = models.DateField (null=True)
    sigungu = models.CharField(max_length=30, null=True)
    dong = models.CharField(max_length=20, null=True)
    # dong = models.CharField(max_length=20, choices=DONG_CHOICES, null=True)
    gpot_id = models.IntegerField(null=True)
    CELL_ID = models.IntegerField(null=True)
    gnb_ID = models.IntegerField(null=True)
    w_lat = models.FloatField(max_length=10, null=True)
    w_lon = models.FloatField(max_length=10, null=True)
    w_ru_id = models.CharField(max_length=10, null=True)
    w_rsrp = models.FloatField(max_length=10, null=True)
    w_rsrq = models.FloatField(max_length=10, null=True)
    w_sinr = models.FloatField(max_length=10, null=True)
    w_cqi = models.FloatField(max_length=10, null=True)
    dist = models.FloatField(max_length=10, null=True)
    # RU_TYPE =  models.FloatField(max_length=10, null=True)
    RANK_INDEX =  models.FloatField(max_length=10, null=True)
    # scg_sum =  models.FloatField(max_length=10, null=True)
    UL_PRB = models.FloatField(max_length=10, null=True)
    DL_PRB = models.FloatField(max_length=10, null=True)
    ul_bler = models.FloatField(max_length=10, null=True)
    dl_bler = models.FloatField(max_length=10, null=True)
    # dl_mcs = models.FloatField(max_length=10, null=True)
    # layer_num = models.FloatField(max_length=10, null=True)
    dl_mcs_layer = models.FloatField(max_length=10, null=True)
    pred_dl_speed = models.FloatField(max_length=10, null=True)
    # created_at = models.DateField(auto_now_add=True, null=True)
    # updated_at =  models.DateField(auto_now = True, null=True)

    class Meta:
        ordering = ['day']

    def get_absolute_url(self):
        return reverse('map:detail')

