# Generated by Django 5.1 on 2024-08-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_fedor_analog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
