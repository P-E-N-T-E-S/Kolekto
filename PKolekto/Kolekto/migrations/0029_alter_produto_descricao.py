# Generated by Django 4.2.5 on 2023-11-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kolekto', '0028_alter_usuario_email_alter_usuario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(max_length=500),
        ),
    ]
