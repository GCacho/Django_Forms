# Generated by Django 4.1 on 2022-08-31 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_clientes_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tfno',
            field=models.CharField(max_length=7, verbose_name='Teléfono'),
        ),
    ]
