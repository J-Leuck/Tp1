# Generated by Django 5.1.1 on 2024-10-01 07:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0005_alter_etape_etape_suivant"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ville",
            old_name="prix",
            new_name="prix_metre2",
        ),
    ]
