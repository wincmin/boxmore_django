# Generated by Django 5.0.6 on 2025-01-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_produto_imagem_alter_produto_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(max_length=100),
        ),
    ]
