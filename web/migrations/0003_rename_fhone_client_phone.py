# Generated by Django 3.2 on 2023-10-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_client_detailorder_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='fhone',
            new_name='phone',
        ),
    ]
