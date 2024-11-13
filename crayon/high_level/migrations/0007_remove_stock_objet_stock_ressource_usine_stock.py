# Generated by Django 5.1.1 on 2024-10-02 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0006_rename_prix_ville_prix_metre2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stock",
            name="objet",
        ),
        migrations.AddField(
            model_name="stock",
            name="ressource",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="high_level.ressource",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usine",
            name="stock",
            field=models.ManyToManyField(to="high_level.stock"),
        ),
    ]