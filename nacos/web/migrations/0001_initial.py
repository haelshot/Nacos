# Generated by Django 4.2.4 on 2023-09-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('100', 'Level 100'), ('200', 'Level 200'), ('300', 'Level 300'), ('400', 'Level 400')], max_length=3)),
                ('title', models.CharField(max_length=200)),
                ('pdf_file', models.FileField(upload_to='course_materials/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='photos/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
