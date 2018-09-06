# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='year_release',
            field=models.IntegerField(default=1998),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='status',
            field=models.CharField(choices=[('Finished', 'Terminato'), ('Ongoing', 'In Corso')], max_length=20, default='In Corso'),
        ),
        migrations.AddField(
            model_name='manga',
            name='year_release',
            field=models.IntegerField(default='1998'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/games/'),
        ),
        migrations.AlterField(
            model_name='game',
            name='vote',
            field=models.CharField(choices=[('Excellent', 'Molto bello'), ('good', 'Buono'), ('normal', 'Normale'), ('bad', 'Brutto'), ('very bad', 'Schifo')], max_length=20, default='normale'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manga',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/manga/'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='vote',
            field=models.CharField(choices=[('Excellent', 'Molto bello'), ('good', 'Buono'), ('normal', 'Normale'), ('bad', 'Brutto'), ('very bad', 'Schifo')], max_length=20, default='Normale'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/profile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to='pic_folder/projects/'),
        ),
    ]
