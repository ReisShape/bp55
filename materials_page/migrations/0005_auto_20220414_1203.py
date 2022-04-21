# Generated by Django 3.1.14 on 2022-04-14 10:03

from django.db import migrations, models
import materials_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_page', '0004_auto_20220202_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(help_text="Datei hochladen. Darf KEINE Umlaute und 'ß' im Namen enthalten!", upload_to='material/', validators=[materials_page.models.validate_pdf_extension, materials_page.models.validate_file_name], verbose_name='Datei'),
        ),
    ]
