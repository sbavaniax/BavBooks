# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Photo', models.ImageField(upload_to=b'')),
                ('Book_Name', models.CharField(max_length=250)),
                ('ISBN_NBR', models.CharField(unique=True, max_length=250)),
                ('PUB_NAME', models.CharField(max_length=250)),
                ('Author_Name', models.CharField(max_length=250)),
                ('Book_Desc', models.TextField()),
                ('Status', models.CharField(default=b'New Book', max_length=1, choices=[(b'N', b'New Book'), (b'H', b'High Rated Book'), (b'M', b'Most Popular Book')])),
                ('Rating', models.CharField(default=1, max_length=1, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('Category', models.CharField(max_length=250)),
                ('Sub_Category', models.CharField(max_length=250)),
                ('download_link', models.URLField(max_length=600)),
            ],
        ),
    ]
