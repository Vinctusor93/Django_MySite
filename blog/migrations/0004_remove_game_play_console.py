# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180906_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='play_console',
        ),
    ]
