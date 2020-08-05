# Generated by Django 3.0.8 on 2020-07-27 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=70, verbose_name='Product Name')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('main_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('img_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('img_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('img_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('prod_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sticky', models.BooleanField(default=False)),
            ],
        ),
    ]
