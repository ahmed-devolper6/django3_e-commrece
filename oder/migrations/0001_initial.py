# Generated by Django 4.1 on 2022-09-28 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.code_grente


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0007_remove_products_qounitiy_alter_reviw_products"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=utils.code_grente.grente_code, max_length=8
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("inprogescss", "inprogescss"),
                            ("complate", "complate"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_cart",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Oders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=utils.code_grente.grente_code, max_length=8
                    ),
                ),
                ("oder_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("deilevry_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("receieved", "receieved"),
                            ("processed", "processed"),
                            ("shiped", "shiped"),
                            ("delivered", "delivered"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_oder",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OderDeitl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                (
                    "oder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oder_detial",
                        to="oder.oders",
                    ),
                ),
                (
                    "proudct",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="oder_proudct",
                        to="products.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartDeitl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_detial",
                        to="oder.cart",
                    ),
                ),
                (
                    "proudct",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cart_proudct",
                        to="products.products",
                    ),
                ),
            ],
        ),
    ]
