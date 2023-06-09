# Generated by Django 4.2 on 2023-05-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('age', models.IntegerField(default=15)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
