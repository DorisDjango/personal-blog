# Generated by Django 4.0.6 on 2022-07-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerwords', models.CharField(max_length=500)),
                ('headerpic', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
