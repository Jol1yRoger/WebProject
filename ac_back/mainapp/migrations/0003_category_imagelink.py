# Generated by Django 4.2.5 on 2024-04-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='imageLink',
            field=models.TextField(default=4232),
            preserve_default=False,
        ),
    ]
