# Generated by Django 3.1.7 on 2021-05-08 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionplanning', '0005_auto_20210508_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacityscheduling',
            name='BalMcOrHour',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='BAL MC/RES HOUR'),
        ),
    ]