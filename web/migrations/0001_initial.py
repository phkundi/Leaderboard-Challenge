# Generated by Django 2.2.7 on 2019-11-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('message', models.TextField(blank=True, default='', max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('copy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FrontpageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('tagline', models.CharField(max_length=70)),
                ('button', models.CharField(max_length=20)),
            ],
        ),
    ]
