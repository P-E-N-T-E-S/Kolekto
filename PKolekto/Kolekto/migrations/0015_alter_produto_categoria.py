# Generated by Django 4.2.5 on 2023-10-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kolekto', '0014_remove_produto_foto2_remove_produto_foto3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[(None, 'Selecione a categoria'), ('moveis', 'Móveis e Decoração'), ('arte', 'Arte'), ('joias', 'Joalheria'), ('livros', 'Livros'), ('relogios', 'Relógios'), ('cartas', 'Cartas'), ('brinquedos', 'Brinquedos e Jogos'), ('roupa', 'Vestuário'), ('foto', 'Fotografia'), ('musica', 'Instrumento Musical'), ('outro', 'Outro')], default=(None, 'Selecione a categoria'), max_length=50),
        ),
    ]