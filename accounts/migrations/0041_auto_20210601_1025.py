# Generated by Django 3.2.3 on 2021-06-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20210531_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='Delivery_Date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='Estimated_Delivery_Date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='PO_Date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
