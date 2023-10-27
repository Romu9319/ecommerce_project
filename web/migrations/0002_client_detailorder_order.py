# Generated by Django 3.2 on 2023-10-10 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10)),
                ('gender', models.CharField(default='M', max_length=1)),
                ('fhone', models.CharField(max_length=20)),
                ('birthday_date', models.DateField(null=True)),
                ('diection', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singup_date', models.DateTimeField(auto_now_add=True)),
                ('number_order', models.CharField(max_length=20, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('state', models.CharField(choices=[('0', 'required'), ('1', 'paid')], default='0', max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.client')),
            ],
        ),
        migrations.CreateModel(
            name='DetailOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuantity', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.product')),
            ],
        ),
    ]
