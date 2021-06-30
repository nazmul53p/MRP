# Generated by Django 3.1.7 on 2021-05-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionplanning', '0006_auto_20210508_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionAndApproval',
            fields=[
                ('id', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Submission And Approval ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data Entry')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Time Entry')),
                ('data_of_submission', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('r_and_d_order_ref_no', models.CharField(blank=True, max_length=32, null=True, verbose_name='R&D / Order Ref. No')),
                ('product_no', models.CharField(blank=True, max_length=32, null=True, verbose_name='Product No.')),
                ('item_description', models.CharField(blank=True, max_length=32, null=True, verbose_name='Item Description')),
                ('color_per_variety', models.CharField(blank=True, max_length=32, null=True, verbose_name='Color / Variety')),
                ('submission_product', models.CharField(blank=True, choices=[('', '---Select---'), ('Raw Mats', 'Raw Mats'), ('Semi - Fin Prod', 'Semi - Fin Prod'), ('Fin Product', 'Fin Product'), ('Others', 'Others')], max_length=32, null=True, verbose_name='Subm Product')),
                ('submission_type', models.CharField(blank=True, choices=[('', '---Select---'), ('Approval', 'Approval'), ('R & D', 'R & D'), ('PP Sample', 'PP Sample'), ('Counter Sample', 'Counter Sample'), ('Shipping Sample', 'Shipping Sample'), ('Test Sample', 'Test Sample'), ('Quality Sample', 'Quality Sample'), ('Color Specimen', 'Color Specimen'), ('Others', 'Others')], max_length=32, null=True, verbose_name='Subm Type')),
                ('submission_item', models.CharField(blank=True, choices=[('', '---Select---'), ('Sample', 'Sample'), ('LD', 'LD'), ('Strike - off', 'Strike - off'), ('K - Down', 'K - Down'), ('MTL', 'MTL'), ('Dyelot', 'Dyelot'), ('Others', 'Others')], max_length=32, null=True, verbose_name='Subm Item')),
                ('item_ref_no', models.CharField(blank=True, max_length=32, null=True, verbose_name='Item Ref No.')),
                ('round_of_submission', models.CharField(blank=True, choices=[('', '---Select---'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('Others', 'Others')], max_length=32, null=True, verbose_name='Round of Submission')),
                ('pland_subm_date', models.DateField(blank=True, max_length=32, null=True, verbose_name='Pland Subm Date')),
                ('submitted_date', models.DateField(blank=True, max_length=32, null=True, verbose_name='Submitted Date')),
                ('result', models.CharField(blank=True, choices=[('', '---Select---'), ('Waiting', 'Waiting'), ('Approved', 'Approved'), ('Appvd with comment', 'Appvd with comment'), ('Rejected', 'Rejected')], max_length=32, null=True, verbose_name='Result')),
                ('comment', models.CharField(blank=True, max_length=32, null=True, verbose_name='Comment')),
                ('approval_or_rejection_date', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
        ),
    ]