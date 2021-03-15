# Generated by Django 3.1.7 on 2021-03-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0009_auto_20210313_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt1', models.CharField(max_length=100)),
                ('img2', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt2', models.CharField(max_length=100)),
                ('img3', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt3', models.CharField(max_length=100)),
                ('img4', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt4', models.CharField(max_length=100)),
                ('img5', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt5', models.CharField(max_length=100)),
                ('img6', models.ImageField(default='default.jpg', upload_to='gallery_images')),
                ('txt6', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.project')),
            ],
        ),
    ]