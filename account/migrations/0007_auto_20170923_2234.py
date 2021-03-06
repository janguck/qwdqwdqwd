# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_delete_userinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_description', models.CharField(max_length=200)),
                ('board_user_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_username', models.IntegerField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('photo_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='action_photo_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Photo'),
        ),
        migrations.AddField(
            model_name='action',
            name='action_user_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
