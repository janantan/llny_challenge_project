# Generated by Django 3.2.6 on 2021-11-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]