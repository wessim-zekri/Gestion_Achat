# Generated by Django 3.1.7 on 2021-05-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210503_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='etat',
            field=models.CharField(choices=[('Terminé', 'Terminé'), ('En cours', 'En cours'), ('Suspendu', 'Suspendu')], max_length=200, null=True),
        ),
    ]
