# Generated by Django 2.0.8 on 2019-01-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0005_auto_20180625_1634'),
        ('residue', '0002_auto_20180504_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Angle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.FloatField()),
                ('b_angle', models.FloatField()),
                ('diff_med', models.FloatField()),
                ('sign_med', models.FloatField(default=0)),
                ('hse', models.IntegerField(default=0)),
                ('sasa', models.FloatField(default=0)),
                ('residue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residue.Residue')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Structure')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='angle',
            unique_together={('residue', 'structure')},
        ),
    ]