# Generated by Django 3.1.7 on 2021-05-02 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210502_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='category',
            new_name='categorie',
        ),
    ]
