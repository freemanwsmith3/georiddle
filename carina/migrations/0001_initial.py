# Generated by Django 5.1.2 on 2024-10-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('image_url', models.URLField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
