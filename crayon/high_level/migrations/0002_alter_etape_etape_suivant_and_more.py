# Generated by Django 5.1.1 on 2024-09-28 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etape",
            name="etape_suivant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="high_level.etape",
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="premiere_etape",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="high_level.etape",
            ),
        ),
    ]
