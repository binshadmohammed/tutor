# Generated by Django 4.1.2 on 2023-04-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_register_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_register',
            name='mobile',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]