# Generated by Django 4.0.4 on 2022-09-05 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0026_profile_nachname_profile_profilbild_profile_vorname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='available_until',
            field=models.DateField(default=datetime.date(2022, 12, 5)),
        ),
    ]
