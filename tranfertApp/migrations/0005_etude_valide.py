# Generated by Django 4.2.6 on 2023-10-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranfertApp', '0004_remove_etudiant_compte_etudiant_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etude',
            name='valide',
            field=models.BooleanField(default=False),
        ),
    ]