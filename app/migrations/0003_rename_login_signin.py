# Generated by Django 4.1.7 on 2023-04-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_signup_rename_created_at_login_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Signin',
        ),
    ]
