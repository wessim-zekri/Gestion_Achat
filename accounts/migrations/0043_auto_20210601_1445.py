# Generated by Django 3.2.3 on 2021-06-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_alter_commande_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='Desired_Delivery_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='Initial_Delivery_Date',
            field=models.DateTimeField(null=True),
        ),
    ]