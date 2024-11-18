# Generated by Django 5.0 on 2024-01-24 16:19

import django.db.models.deletion
import profs.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('contact_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to=profs.models.user_directory_path)),
                ('skills', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='RelationshipManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('assigned_students', models.ManyToManyField(related_name='assigned_relationship_managers', to='profs.studentprofile')),
            ],
            options={
                'verbose_name_plural': 'Mentors',
            },
        ),
    ]
