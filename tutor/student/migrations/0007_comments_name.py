# Generated by Django 4.1.2 on 2023-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
