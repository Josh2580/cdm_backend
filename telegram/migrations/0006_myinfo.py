# Generated by Django 5.0.3 on 2024-03-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0005_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Shady', max_length=255, unique=True)),
                ('api_key', models.CharField(default='api-key-123', max_length=1055, unique=True)),
            ],
        ),
    ]
