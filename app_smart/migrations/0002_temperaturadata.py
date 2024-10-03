# Generated by Django 5.0.7 on 2024-10-03 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperaturaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
    ]
