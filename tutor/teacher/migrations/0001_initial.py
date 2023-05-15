# Generated by Django 4.1.2 on 2023-03-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]
