# Generated by Django 4.0.6 on 2022-07-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.CharField(db_index=True, max_length=200)),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('genre', models.ManyToManyField(to='backend.genre')),
            ],
        ),
    ]
