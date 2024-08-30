# Generated by Django 5.1 on 2024-08-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iziskill', '0009_room_messager'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('draft', 'Draft')], default='draft', max_length=20, verbose_name='Statut'),
        ),
    ]
