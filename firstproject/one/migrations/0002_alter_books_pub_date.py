# Generated by Django 3.2.7 on 2021-09-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
