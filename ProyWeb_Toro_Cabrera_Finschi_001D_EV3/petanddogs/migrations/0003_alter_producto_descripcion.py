# Generated by Django 5.0.6 on 2024-06-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petanddogs', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=5000),
        ),
    ]
