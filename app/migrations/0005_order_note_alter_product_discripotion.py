# Generated by Django 4.0.4 on 2022-07-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discripotion',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
