# Generated by Django 2.0.8 on 2019-01-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactnetwork', '0004_auto_20190122_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distance',
            name='distance',
            field=models.IntegerField(),
        ),
    ]
