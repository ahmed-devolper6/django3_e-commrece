# Generated by Django 4.1 on 2022-10-23 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_remove_products_qounitiy_alter_reviw_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviw",
            name="products",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Proudct_Review",
                to="products.products",
                verbose_name="product",
            ),
        ),
    ]
