# Generated by Django 4.2 on 2023-07-31 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_all_stock_underlying'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolumeGainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_json', models.TextField()),
            ],
        ),
    ]