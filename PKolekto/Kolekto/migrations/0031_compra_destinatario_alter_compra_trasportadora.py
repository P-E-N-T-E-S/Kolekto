# Generated by Django 4.2.5 on 2023-11-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0030_compra"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="destinatario",
            field=models.CharField(default="padrao", max_length=100),
        ),
        migrations.AlterField(
            model_name="compra",
            name="trasportadora",
            field=models.CharField(max_length=100),
        ),
    ]
