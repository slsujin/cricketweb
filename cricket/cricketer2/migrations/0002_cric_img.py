# Generated by Django 4.1.7 on 2023-03-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketer2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cric',
            name='img',
            field=models.ImageField(default='dfdggf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]