# Generated by Django 4.0.4 on 2022-06-21 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0018_profile_searchradius'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='available_until',
            field=models.DateField(default=datetime.date(2022, 9, 21)),
        ),
    ]
