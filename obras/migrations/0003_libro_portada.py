# Generated by Django 4.0.4 on 2022-05-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(null=True, upload_to='avatares'),
        ),
    ]
