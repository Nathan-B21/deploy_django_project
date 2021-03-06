# Generated by Django 2.2.4 on 2021-04-01 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enemy_name', models.CharField(max_length=20)),
                ('max_health', models.IntegerField()),
                ('health', models.IntegerField()),
                ('max_attack', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Knight',
            fields=[
                ('character_name', models.CharField(max_length=10)),
                ('max_health', models.IntegerField()),
                ('health', models.IntegerField()),
                ('max_attack', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='game_app.User')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('character_name', models.CharField(max_length=45)),
                ('max_health', models.IntegerField()),
                ('health', models.IntegerField()),
                ('max_attack', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('max_magic', models.IntegerField()),
                ('magic', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='game_app.User')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rogue',
            fields=[
                ('character_name', models.CharField(max_length=45)),
                ('max_health', models.IntegerField()),
                ('health', models.IntegerField()),
                ('max_attack', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='game_app.User')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
