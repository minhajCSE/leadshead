# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.CharField(max_length=50)),
                ('date', models.DateField(default=None)),
                ('payment_method', models.CharField(max_length=30)),
                ('coupon', models.CharField(max_length=20)),
                ('is_send', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
