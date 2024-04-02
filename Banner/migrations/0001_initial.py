# Generated by Django 5.0.3 on 2024-04-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_en', models.CharField(max_length=200)),
                ('description_ru', models.CharField(max_length=200)),
                ('description_uz', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('name_ru', models.CharField(max_length=200)),
                ('name_uz', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image_file', models.ImageField(upload_to='banner/')),
            ],
        ),
    ]
