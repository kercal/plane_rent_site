# Generated by Django 4.0.4 on 2022-06-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0013_remove_annonce_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='kategorie',
            field=models.ManyToManyField(blank=True, null=True, to='annoncen.kategorie'),
        ),
    ]