# Generated by Django 3.1.7 on 2021-05-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_projet_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='durée_semaines',
            field=models.PositiveIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='quntite_piece',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]