# Generated by Django 5.1.4 on 2025-03-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnippet',
            name='desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
