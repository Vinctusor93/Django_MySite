# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180906_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='play_console',
            field=models.CharField(default='ps1', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(default='https://github.com/Vinctusor93/Django_MySite'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='year_release',
            field=models.IntegerField(validators=[blog.validators.validate_year]),
        ),
        migrations.AlterField(
            model_name='manga',
            name='year_release',
            field=models.IntegerField(validators=[blog.validators.validate_year]),
        ),
    ]
