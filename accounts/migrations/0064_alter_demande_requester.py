# Generated by Django 3.2 on 2021-06-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20210610_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='Requester',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
