# Generated by Django 3.1.7 on 2021-03-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0008_auto_20210313_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, default='fa fa-', max_length=100),
        ),
    ]
