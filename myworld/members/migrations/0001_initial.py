# Generated by Django 3.2.9 on 2022-04-29 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
                ('image_link', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.user')),
            ],
        ),
    ]
