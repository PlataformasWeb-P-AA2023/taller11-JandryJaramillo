# Generated by Django 4.2.2 on 2023-07-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0002_rename_nombre_departamento_nombrep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='costo',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='numCuartos',
            field=models.IntegerField(),
        ),
    ]
