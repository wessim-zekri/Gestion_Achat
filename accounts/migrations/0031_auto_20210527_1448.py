# Generated by Django 3.2.3 on 2021-05-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_fournisseur_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='accounts')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='fournisseur',
            name='activated',
        ),
        migrations.RemoveField(
            model_name='fournisseur',
            name='file_name',
        ),
    ]
