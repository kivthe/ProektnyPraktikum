# Generated by Django 5.0.6 on 2024-10-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_rentridecar_id_alter_rentridecar_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carlosoncar',
            name='id',
        ),
        migrations.AlterField(
            model_name='carlosoncar',
            name='link',
            field=models.CharField(default='Unknown', max_length=512, primary_key=True, serialize=False),
        ),
    ]
