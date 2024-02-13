# Generated by Django 5.0.2 on 2024-02-12 11:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('graduation_year', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('period', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('intro', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='profile_pics/')),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('github_url', models.URLField()),
                ('imple1', models.CharField(max_length=25)),
                ('imple2', models.CharField(max_length=25)),
                ('imple3', models.CharField(max_length=25)),
                ('imple4', models.CharField(max_length=25)),
                ('imple5', models.CharField(max_length=25)),
                ('imple6', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]