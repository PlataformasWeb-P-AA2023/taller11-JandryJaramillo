# Generated by Django 4.2.2 on 2023-07-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0003_alter_departamento_costo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='costo',
            field=models.FloatField(),
        ),
    ]
