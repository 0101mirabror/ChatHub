# Generated by Django 4.2.6 on 2023-11-25 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('time', models.TimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chatapp.userprofile')),
                ('sender_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='chatapp.userprofile')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.userprofile')),
            ],
        ),
    ]
