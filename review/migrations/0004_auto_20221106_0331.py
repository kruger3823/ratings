# Generated by Django 2.1.9 on 2022-11-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20221106_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comments',
            field=models.TextField(verbose_name='TIMELINES'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments1',
            field=models.TextField(verbose_name='PARTIALITY'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments2',
            field=models.TextField(verbose_name='PUNCTUALITY'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments3',
            field=models.TextField(verbose_name='LOUDNESS'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments4',
            field=models.TextField(verbose_name='UNDERSTANDABLE'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments5',
            field=models.TextField(verbose_name='DOUBT CLARITY'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments6',
            field=models.TextField(verbose_name='PATIENCE'),
        ),
    ]
