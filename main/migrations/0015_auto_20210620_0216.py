# Generated by Django 3.2.2 on 2021-06-19 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_chat_id_message_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ucheniki',
            name='nomdog',
        ),
        migrations.RemoveField(
            model_name='ucheniki',
            name='nomspravki',
        ),
    ]