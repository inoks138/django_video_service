# Generated by Django 4.0.4 on 2022-05-26 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, unique=True, verbose_name='Название')),
                ('required_age', models.IntegerField(verbose_name='Требуемый возраст')),
            ],
            options={
                'verbose_name': 'Возрастное ограничение',
                'verbose_name_plural': 'Возрастные ограничения',
                'ordering': ['required_age'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.SlugField(max_length=115, unique=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('type', models.CharField(choices=[('film', 'film'), ('series', 'series')], default='film', max_length=6, verbose_name='Тип')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('poster', models.ImageField(upload_to='movie_posters/%Y/%m/%d', verbose_name='Постер')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='Страна')),
                ('budget', models.IntegerField(blank=True, help_text='Указывать в долларах', null=True, verbose_name='Бюджет')),
                ('is_released', models.BooleanField(default=True, help_text='Вышло ли уже кино', verbose_name='Выпущено')),
                ('require_subscription', models.BooleanField(default=False, verbose_name='Нужна подписка')),
                ('require_purchase', models.BooleanField(default=False, verbose_name='Нужна покупка')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('age_limit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.agelimit', verbose_name='Возрастное ограничение')),
            ],
            options={
                'verbose_name': 'Кино',
                'verbose_name_plural': 'Кино',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PersonRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название')),
                ('number', models.IntegerField(verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'Сезоны',
                'ordering': ['series', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('movie_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='movies.movie')),
                ('video', models.FileField(upload_to='films/%Y/%m/%d', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
            bases=('movies.movie',),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('movie_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='movies.movie')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
            bases=('movies.movie',),
        ),
        migrations.CreateModel(
            name='Trailers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='movie_trailers/%Y/%m/%d', verbose_name='Видео')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Кино')),
            ],
            options={
                'verbose_name': 'Трейлер',
                'verbose_name_plural': 'Трейлеры',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('roles', models.ManyToManyField(to='movies.personrole', verbose_name='Роли')),
            ],
            options={
                'verbose_name': 'Личность',
                'verbose_name_plural': 'Личности',
            },
        ),
        migrations.CreateModel(
            name='MovieImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie_images', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Кино')),
            ],
            options={
                'verbose_name': 'Фотография из фильма',
                'verbose_name_plural': 'Фотографии из фильма',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director_movies', to='movies.person', verbose_name='Режиссер'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='movie',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writer_movies', to='movies.person', verbose_name='Сценарист'),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='series/%Y/%m/%d', verbose_name='Видео')),
                ('title', models.CharField(blank=True, max_length=75, null=True, verbose_name='Название')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='movies.season', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
                'ordering': ['season', 'number'],
            },
        ),
        migrations.AddField(
            model_name='season',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='movies.series', verbose_name='Сериал'),
        ),
    ]
