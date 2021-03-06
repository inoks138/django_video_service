# Generated by Django 4.0.4 on 2022-05-27 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import movies.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='video',
            field=models.FileField(upload_to='series/%Y/%m/%d', validators=[movies.validators.validate_video_file], verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.FileField(upload_to='films/%Y/%m/%d', validators=[movies.validators.validate_video_file], verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='movieimages',
            name='image',
            field=models.ImageField(upload_to='movie_images/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='trailers',
            name='video',
            field=models.FileField(upload_to='movie_trailers/%Y/%m/%d', validators=[movies.validators.validate_video_file], verbose_name='Видео'),
        ),
        migrations.CreateModel(
            name='MovieRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Оценка')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='movies.movie', verbose_name='Кино')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
                'ordering': ['movie'],
            },
        ),
    ]
