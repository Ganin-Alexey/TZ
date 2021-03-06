# Generated by Django 2.2.10 on 2021-07-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interrogation', '0006_auto_20210703_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interrogation',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Активный?'),
        ),
        migrations.AlterField(
            model_name='interrogation',
            name='stop',
            field=models.DateTimeField(blank=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='question',
            name='interrogation',
            field=models.ForeignKey(default=0, on_delete='CASCADE', related_name='questions', to='interrogation.Interrogation', verbose_name='Опрос'),
        ),
    ]
