# Generated by Django 3.1.7 on 2021-05-17 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionplanning', '0007_submissionandapproval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissionandapproval',
            name='id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Submission And Approval ID'),
        ),
    ]