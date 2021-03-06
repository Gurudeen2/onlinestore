# Generated by Django 3.0.8 on 2020-07-29 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=200)),
                ('prod_id', models.IntegerField()),
                ('username', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('cart_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
