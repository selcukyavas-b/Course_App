# Generated by Django 5.1.1 on 2024-09-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
