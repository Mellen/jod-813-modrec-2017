# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_date', models.DateTimeField(verbose_name='date accepted')),
                ('username', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='ConsentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='consentanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.ConsentQuestion'),
        ),
    ]