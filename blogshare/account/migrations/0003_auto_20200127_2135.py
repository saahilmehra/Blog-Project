# Generated by Django 3.0.2 on 2020-01-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200127_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]