# Generated by Django 3.0.7 on 2020-08-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200831_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpo_registeration',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
