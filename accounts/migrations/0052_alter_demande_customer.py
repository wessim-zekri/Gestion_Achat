# Generated by Django 3.2.3 on 2021-06-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20210604_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='Customer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
