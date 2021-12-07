# Generated by Django 3.2.9 on 2021-12-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
