# Generated by Django 4.1.7 on 2023-10-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kimchi', '0004_delete_storydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
