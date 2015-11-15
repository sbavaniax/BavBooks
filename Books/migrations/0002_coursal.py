# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Photo1', models.ImageField(upload_to=b'')),
                ('Photot2', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
