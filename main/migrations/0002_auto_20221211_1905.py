# Generated by Django 3.2.16 on 2022-12-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Експонат', 'verbose_name_plural': 'Експонати'},
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.CharField(default='2022', max_length=4, verbose_name='Рік видання'),
        ),
    ]
