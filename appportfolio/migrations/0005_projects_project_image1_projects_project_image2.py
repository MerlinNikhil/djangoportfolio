# Generated by Django 5.0.2 on 2024-02-14 11:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0004_remove_projects_desc_projects_lifecycle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_image1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='proj_pics/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='project_image2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='proj_pics/'),
            preserve_default=False,
        ),
    ]
