# Generated by Django 2.2.10 on 2021-07-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interrogation', '0008_auto_20210703_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(max_length=4096),
        ),
    ]