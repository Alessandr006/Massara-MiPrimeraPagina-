# Generated by Django 5.2 on 2025-04-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_publicacion_fecha_publicacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
