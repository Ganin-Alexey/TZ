# Generated by Django 2.2.10 on 2021-07-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interrogation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interrogation',
            name='interrogation_self',
        ),
        migrations.AddField(
            model_name='interrogation',
            name='questions',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete='CASCADE', related_name='questions', to='interrogation.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='interrogation',
            field=models.ForeignKey(default=0, on_delete='CASCADE', related_name='interrogations', to='interrogation.Interrogation', verbose_name='Опрос'),
        ),
    ]