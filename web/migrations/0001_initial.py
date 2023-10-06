# Generated by Django 3.2 on 2023-10-06 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
        ),
    ]
