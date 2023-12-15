# Generated by Django 4.2.4 on 2023-11-16 12:10

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_remove_producto_categoria_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='talla',
        ),
        migrations.CreateModel(
            name='Prod_Calzado',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tienda.producto')),
                ('talla', multiselectfield.db.fields.MultiSelectField(choices=[('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54')], max_length=56)),
            ],
            bases=('tienda.producto',),
        ),
        migrations.CreateModel(
            name='Prod_Ropa',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tienda.producto')),
                ('talla', multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=8)),
            ],
            bases=('tienda.producto',),
        ),
    ]