# Generated by Django 4.2.5 on 2023-11-21 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0036_avaliacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="avaliacao",
            name="produto",
        ),
        migrations.AddField(
            model_name="avaliacao",
            name="loja",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Kolekto.loja",
            ),
        ),
    ]
