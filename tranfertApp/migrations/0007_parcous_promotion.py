# Generated by Django 4.2.6 on 2023-10-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranfertApp', '0006_alter_etudiant_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcous',
            name='promotion',
            field=models.CharField(default='L4 MSI', max_length=30),
        ),
    ]