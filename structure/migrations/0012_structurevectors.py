# Generated by Django 2.0.8 on 2019-04-10 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0011_structurecomplexprotein'),
    ]

    operations = [
        migrations.CreateModel(
            name='StructureVectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_axis', models.CharField(max_length=100)),
                ('tm1_axis', models.CharField(max_length=100)),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Structure')),
            ],
            options={
                'db_table': 'structure_vectors',
            },
        ),
    ]