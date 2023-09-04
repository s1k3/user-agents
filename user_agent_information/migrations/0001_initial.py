# Generated by Django 4.2.4 on 2023-08-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.TextField(max_length=500)),
                ('os', models.CharField(max_length=500)),
                ('device', models.CharField(max_length=500)),
                ('is_tablet', models.BooleanField()),
                ('is_pc', models.BooleanField()),
                ('is_mobile', models.BooleanField()),
                ('is_touch_capable', models.BooleanField()),
                ('is_bot', models.BooleanField()),
            ],
        ),
    ]