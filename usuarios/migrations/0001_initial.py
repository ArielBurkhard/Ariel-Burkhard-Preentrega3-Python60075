# Generated by Django 5.1.1 on 2024-11-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('e_mail', models.CharField(max_length=8)),
                ('contrasenia', models.CharField(max_length=80)),
            ],
        ),
    ]
