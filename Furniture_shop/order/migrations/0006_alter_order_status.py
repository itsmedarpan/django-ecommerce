# Generated by Django 5.2.1 on 2025-07-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('ordered', 'Ordered')], default='ordered', max_length=20),
        ),
    ]
