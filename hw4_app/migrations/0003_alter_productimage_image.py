# Generated by Django 5.0.2 on 2024-02-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw4_app', '0002_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
