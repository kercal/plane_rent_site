# Generated by Django 4.0.4 on 2022-06-21 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0019_alter_annonce_available_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='available_until',
            field=models.DateField(blank=True, default=datetime.date(2022, 9, 21), null=True),
        ),
    ]
