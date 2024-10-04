# Generated by Django 5.0.6 on 2024-10-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=128)),
                ('shipper', models.CharField(default='', max_length=128)),
                ('price', models.IntegerField(default=-1)),
                ('price_currency', models.CharField(default='USD', max_length=32)),
            ],
        ),
    ]
