# Generated by Django 4.1 on 2022-09-28 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_remove_products_qounitiy_alter_reviw_products"),
        ("oder", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartdeitl",
            old_name="quantity",
            new_name="quantiity",
        ),
        migrations.RenameField(
            model_name="oderdeitl",
            old_name="quantity",
            new_name="quantiity",
        ),
        migrations.AddField(
            model_name="oderdeitl",
            name="total",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cart",
            name="status",
            field=models.CharField(
                choices=[("inprogecss", "inprogecss"), ("compalted", "compalted")],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="cartdeitl",
            name="cart",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cart_detail",
                to="oder.cart",
            ),
        ),
        migrations.AlterField(
            model_name="cartdeitl",
            name="proudct",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_cart",
                to="products.products",
            ),
        ),
        migrations.AlterField(
            model_name="oderdeitl",
            name="oder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="oder_detail",
                to="oder.oders",
            ),
        ),
        migrations.AlterField(
            model_name="oderdeitl",
            name="proudct",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_oder",
                to="products.products",
            ),
        ),
        migrations.AlterField(
            model_name="oders",
            name="status",
            field=models.CharField(
                choices=[
                    ("receieved", "receieved"),
                    ("processed", "processed"),
                    ("shiped", "shiped"),
                    ("delivered", "delivered"),
                ],
                max_length=15,
            ),
        ),
    ]
