# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cartells.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activa', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enviament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('telefon', models.DecimalField(max_digits=9, decimal_places=0)),
                ('data', models.DateTimeField(verbose_name=b'data de carrega')),
                ('titol', models.CharField(max_length=100)),
                ('arxiu', models.FileField(upload_to=cartells.models.filebuilder)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cartell',
            fields=[
                ('enviament_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cartells.Enviament')),
            ],
            options={
            },
            bases=('cartells.enviament',),
        ),
        migrations.CreateModel(
            name='Assaig',
            fields=[
                ('enviament_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cartells.Enviament')),
            ],
            options={
            },
            bases=('cartells.enviament',),
        ),
        migrations.CreateModel(
            name='Narracio',
            fields=[
                ('enviament_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cartells.Enviament')),
            ],
            options={
            },
            bases=('cartells.enviament',),
        ),
        migrations.CreateModel(
            name='Poesia',
            fields=[
                ('enviament_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cartells.Enviament')),
            ],
            options={
            },
            bases=('cartells.enviament',),
        ),
    ]
