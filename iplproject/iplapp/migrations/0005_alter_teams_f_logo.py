# Generated by Django 5.0.4 on 2024-04-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0004_alter_teams_f_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='f_logo',
            field=models.FileField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
