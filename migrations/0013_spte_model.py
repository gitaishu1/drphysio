# Generated by Django 5.2.1 on 2025-06-02 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_mmtmotion_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPTE_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testname', models.CharField(max_length=200)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.patient_model')),
            ],
            options={
                'db_table': 'ST',
            },
        ),
    ]
