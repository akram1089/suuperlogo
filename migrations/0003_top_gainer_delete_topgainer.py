# Generated by Django 4.2 on 2023-06-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_topgainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Gainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_gainers', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='TopGainer',
        ),
    ]
