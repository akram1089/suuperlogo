# Generated by Django 4.2 on 2023-07-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='symbol_name',
            field=models.CharField(max_length=100),
        ),
    ]