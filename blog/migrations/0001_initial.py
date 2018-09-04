# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=60)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='static/blog/pic_folder/manga/')),
                ('description', models.TextField()),
                ('vote', models.CharField(max_length=20, default='normale', choices=[('Excellent', 'Molto bello'), ('good', 'buono'), ('normal', 'normale'), ('bad', 'brutto'), ('very bad', 'schifo')])),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('genre', models.CharField(max_length=60)),
                ('product_factory', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='static/blog/pic_folder/games/')),
                ('description', models.TextField()),
                ('vote', models.CharField(max_length=20, default='normale', choices=[('Excellent', 'Molto bello'), ('good', 'buono'), ('normal', 'normale'), ('bad', 'brutto'), ('very bad', 'schifo')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('photo', models.ImageField(upload_to='static/blog/pic_folder/profile/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('argument', models.CharField(max_length=60)),
                ('group', models.CharField(max_length=60)),
                ('tecnologies', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='static/blog/pic_folder/projects/')),
                ('description', models.TextField()),
            ],
        ),
    ]
