# Generated by Django 5.1.2 on 2024-10-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('ConfirmPassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
