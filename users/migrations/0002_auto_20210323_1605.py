# Generated by Django 3.1.7 on 2021-03-23 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=5)),
                ('district', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('complement', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, default='Guarapuava', max_length=30)),
                ('state', models.CharField(blank=True, default='Paraná', max_length=30)),
            ],
            options={
                'verbose_name': 'Endereços',
                'verbose_name_plural': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.adress')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]