# Generated by Django 4.2.6 on 2023-10-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=20, verbose_name='марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'white'), ('black', 'black'), ('blue', 'blue'), ('red', 'red')], max_length=20, verbose_name='цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='cost',
            field=models.IntegerField(blank=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, verbose_name='год выпуска'),
        ),
    ]
