# Generated by Django 4.0.6 on 2022-07-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('byline', models.CharField(help_text='Just a small summary or main point of the post', max_length=500)),
                ('slug', models.SlugField()),
                ('post_image', models.ImageField(blank=True, upload_to='images')),
                ('text', models.TextField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
