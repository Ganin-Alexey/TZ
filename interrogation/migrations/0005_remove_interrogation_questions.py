# Generated by Django 2.2.10 on 2021-07-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interrogation', '0004_auto_20210702_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interrogation',
            name='questions',
        ),
    ]
