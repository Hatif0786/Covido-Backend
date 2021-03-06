# Generated by Django 3.1.4 on 2021-05-04 21:17

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('Name', models.CharField(max_length=20)),
                ('Suggestion', models.TextField(blank=True, default=' ')),
            ],
        ),
    ]
