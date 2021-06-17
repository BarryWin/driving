# Generated by Django 3.2.2 on 2021-06-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sotrudniki',
            name='fam',
            field=models.CharField(default='', max_length=250, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='sotrudniki',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='sotrudniki',
            name='otch',
            field=models.CharField(default='', max_length=250, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='ucheniki',
            name='fam',
            field=models.CharField(default='', max_length=250, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='ucheniki',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='ucheniki',
            name='otch',
            field=models.CharField(default='', max_length=250, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='stoimostobuch',
            field=models.PositiveIntegerField(verbose_name='Стоимость обучения'),
        ),
        migrations.AlterField(
            model_name='sotrudniki',
            name='fio',
            field=models.CharField(max_length=250, verbose_name='ФИО'),
        ),
    ]