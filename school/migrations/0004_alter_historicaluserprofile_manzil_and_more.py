# Generated by Django 4.2.15 on 2024-09-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_historicaluserprofile_born_in_userprofile_born_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='manzil',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='manzil',
            field=models.CharField(max_length=512),
        ),
    ]