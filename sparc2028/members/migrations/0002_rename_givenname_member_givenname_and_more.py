# Generated by Django 5.1.1 on 2024-09-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='givenname',
            new_name='givenName',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='lastName',
        ),
        migrations.RemoveField(
            model_name='member',
            name='middleinitial',
        ),
        migrations.AddField(
            model_name='member',
            name='creativesTeam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='externalsTeam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='potdTeam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='reviewerTeam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='middleInitial',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
