# Generated by Django 4.1 on 2022-09-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='qounitiy',
            field=models.IntegerField(default=50),
        ),
    ]
