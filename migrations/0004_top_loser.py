# Generated by Django 4.2 on 2023-06-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_top_gainer_delete_topgainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Loser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_losers', models.TextField()),
            ],
        ),
    ]
