# Generated by Django 4.2.6 on 2023-10-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('edition', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(related_name='books', to='books.author')),
            ],
        ),
    ]
