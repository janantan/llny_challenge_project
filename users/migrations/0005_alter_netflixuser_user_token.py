# Generated by Django 3.2.6 on 2021-11-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211115_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflixuser',
            name='user_token',
            field=models.CharField(default='90fe78c9', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]