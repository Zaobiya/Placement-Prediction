# Generated by Django 5.0 on 2024-02-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('relationship_manager', 'Relationship Manager')], default='student', max_length=20),
        ),
    ]