# Generated by Django 5.2.1 on 2025-06-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0030_apppointment_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('contactnumber', models.IntegerField()),
                ('Clinicname', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
