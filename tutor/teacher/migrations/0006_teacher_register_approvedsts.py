# Generated by Django 4.1.7 on 2023-05-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_alter_teacher_register_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_register',
            name='approvedsts',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]