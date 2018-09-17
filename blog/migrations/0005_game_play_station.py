# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_game_play_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='play_station',
            field=models.CharField(default='ps1', max_length=60),
            preserve_default=False,
        ),
    ]
