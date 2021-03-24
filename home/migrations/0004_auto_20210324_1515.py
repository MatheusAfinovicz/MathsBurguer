# Generated by Django 3.1.7 on 2021-03-24 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210323_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(max_length=1500, verbose_name='Mensagem'),
        ),
    ]
