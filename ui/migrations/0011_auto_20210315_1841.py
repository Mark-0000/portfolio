# Generated by Django 3.1.7 on 2021-03-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0010_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='txt1',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='txt2',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='txt3',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='txt4',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='txt5',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='txt6',
            field=models.CharField(blank=True, default='NULL', max_length=100),
        ),
    ]
