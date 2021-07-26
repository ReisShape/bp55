# Generated by Django 3.1.5 on 2021-03-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_page', '0002_auto_20210309_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materialien'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Sonstiges', help_text='Bezeichnung der Kategorie', max_length=1000, verbose_name='Titel'),
        ),
    ]