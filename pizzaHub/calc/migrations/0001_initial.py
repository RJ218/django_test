# Generated by Django 3.1 on 2020-09-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_img', models.TextField()),
                ('movie_createdate', models.CharField(max_length=100)),
                ('movie_releasedate', models.CharField(max_length=100)),
                ('movie_descrip', models.TextField()),
            ],
        ),
    ]
