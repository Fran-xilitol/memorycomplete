# Generated by Django 3.1.4 on 2021-01-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameness', '0005_auto_20201229_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turn',
            name='hold_card',
        ),
        migrations.RemoveField(
            model_name='turn',
            name='open_turn',
        ),
        migrations.AddField(
            model_name='game',
            name='hold_card',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='game',
            name='open_turn',
            field=models.BooleanField(default=False),
        ),
    ]
