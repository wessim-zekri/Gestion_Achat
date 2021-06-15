# Generated by Django 3.2.3 on 2021-06-10 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0061_auto_20210610_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='Request',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.demande_validée'),
        ),
        migrations.AlterField(
            model_name='demande_validée',
            name='demande',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.demande'),
        ),
        migrations.DeleteModel(
            name='Demande_Non_Validée',
        ),
    ]
