# Generated by Django 3.2.13 on 2022-08-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Name', max_length=25)),
                ('lastname', models.CharField(default='Name', max_length=25)),
                ('password1', models.CharField(default='PW1', max_length=25)),
                ('password2', models.CharField(default='Confirm', max_length=25)),
                ('usrphone', models.TextField(default='934')),
                ('username', models.CharField(default='Name', max_length=25)),
            ],
        ),
    ]
