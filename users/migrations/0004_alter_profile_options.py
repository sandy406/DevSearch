# Generated by Django 4.2.3 on 2023-08-05 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_social_twitter_profile_social_youtube'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
