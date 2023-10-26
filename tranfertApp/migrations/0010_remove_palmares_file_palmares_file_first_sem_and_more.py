# Generated by Django 4.2.6 on 2023-10-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranfertApp', '0009_palmares_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palmares',
            name='file',
        ),
        migrations.AddField(
            model_name='palmares',
            name='file_first_sem',
            field=models.FileField(null=True, upload_to='palmares1'),
        ),
        migrations.AddField(
            model_name='palmares',
            name='file_second_sem',
            field=models.FileField(null=True, upload_to='palmares2'),
        ),
    ]
