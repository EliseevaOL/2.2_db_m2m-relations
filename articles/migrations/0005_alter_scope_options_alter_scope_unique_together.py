# Generated by Django 5.0.1 on 2024-05-25 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_tags_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Tematika statii'},
        ),
        migrations.AlterUniqueTogether(
            name='scope',
            unique_together=set(),
        ),
    ]