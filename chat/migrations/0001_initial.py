# Generated by Django 3.0.5 on 2020-04-17 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('username', models.TextField(default='anonymous')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='message_room', to='chat.Room')),
            ],
        ),
    ]
