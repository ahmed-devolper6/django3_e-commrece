# Generated by Django 4.1 on 2022-09-19 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_reviw_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='qounitiy',
        ),
        migrations.AlterField(
            model_name='reviw',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products', verbose_name='product'),
        ),
    ]
