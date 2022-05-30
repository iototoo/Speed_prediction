# Generated by Django 4.0.4 on 2022-05-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('day', models.IntegerField(null=True)),
                ('sigungu', models.CharField(max_length=30, null=True)),
                ('dong', models.CharField(max_length=20, null=True)),
                ('gpot_id', models.IntegerField(null=True)),
                ('CELL_ID', models.IntegerField(null=True)),
                ('gnb_ID', models.IntegerField(null=True)),
                ('w_lat', models.FloatField(max_length=10, null=True)),
                ('w_lon', models.FloatField(max_length=10, null=True)),
                ('w_ru_id', models.CharField(max_length=10, null=True)),
                ('w_rsrp', models.FloatField(max_length=10, null=True)),
                ('w_rsrq', models.FloatField(max_length=10, null=True)),
                ('w_sinr', models.FloatField(max_length=10, null=True)),
                ('w_cqi', models.FloatField(max_length=10, null=True)),
                ('dist', models.FloatField(max_length=10, null=True)),
                ('RANK_INDEX', models.FloatField(max_length=10, null=True)),
                ('UL_PRB', models.FloatField(max_length=10, null=True)),
                ('DL_PRB', models.FloatField(max_length=10, null=True)),
                ('ul_bler', models.FloatField(max_length=10, null=True)),
                ('dl_bler', models.FloatField(max_length=10, null=True)),
                ('dl_mcs_layer', models.FloatField(max_length=10, null=True)),
                ('pred_dl_speed', models.FloatField(max_length=10, null=True)),
            ],
            options={
                'ordering': ['day'],
            },
        ),
    ]