# Generated by Django 4.2.5 on 2023-09-29 16:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0009_remove_produto_loja_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loja",
            old_name="dados_contato",
            new_name="descricao",
        ),
    ]
