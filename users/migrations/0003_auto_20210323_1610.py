# Generated by Django 3.1.7 on 2021-03-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210323_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useradress',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='useradress',
            name='user',
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
        migrations.DeleteModel(
            name='UserAdress',
        ),
    ]
