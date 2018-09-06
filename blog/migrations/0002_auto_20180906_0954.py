# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.ImageField(upload_to='static/pic_folder/games/'),
        ),
        migrations.AlterField(
            model_name='game',
            name='vote',
            field=models.CharField(default='normale', choices=[('Excellent', 'Molto bello'), ('good', 'Buono'), ('normal', 'normale'), ('bad', 'Brutto'), ('very bad', 'Schifo')], max_length=20),
        ),
        migrations.AlterField(
            model_name='manga',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/manga/'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='vote',
            field=models.CharField(default='normale', choices=[('Excellent', 'Molto bello'), ('good', 'Buono'), ('normal', 'normale'), ('bad', 'Brutto'), ('very bad', 'Schifo')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/profile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to='static/pic_folder/projects/'),
        ),
    ]
