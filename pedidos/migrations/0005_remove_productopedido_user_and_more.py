# Generated by Django 4.2.4 on 2023-12-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_direcciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productopedido',
            name='user',
        ),
        migrations.AlterField(
            model_name='direcciones',
            name='codigoPostal',
            field=models.IntegerField(),
        ),
    ]
