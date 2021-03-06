# Generated by Django 3.1.7 on 2021-07-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/person')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
    ]
