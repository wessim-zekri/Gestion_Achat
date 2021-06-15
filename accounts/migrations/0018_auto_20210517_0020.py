# Generated by Django 3.1.7 on 2021-05-16 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_commande_demande_non_validée_demande_validée_employé_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employé',
            name='session',
        ),
        migrations.AddField(
            model_name='employé',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employé',
            name='telephone',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='telephone',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='durée_en_semaines',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
