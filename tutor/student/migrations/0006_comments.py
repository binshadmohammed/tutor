# Generated by Django 4.1.2 on 2023-04-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_booking_tfee_booking_tmobile_booking_tname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=200)),
                ('t_id', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('sdate', models.CharField(max_length=200)),
            ],
        ),
    ]
