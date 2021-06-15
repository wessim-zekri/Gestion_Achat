# Generated by Django 3.2.3 on 2021-06-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_alter_commande_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='Application_Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='Initial_Cost_Cotation',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='Num_RFQ',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='PO_Customer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='Quotation_Number',
            field=models.IntegerField(null=True),
        ),
    ]