# Generated by Django 5.0.6 on 2024-06-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petanddogs', '0003_alter_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=128)),
                ('activo', models.IntegerField()),
            ],
        ),
    ]