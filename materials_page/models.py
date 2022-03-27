"""
Configurations for the Database Models for the App 'materials_page'
"""

# pylint: disable=import-outside-toplevel
from django.core.exceptions import ValidationError
from django.db import models


def validate_pdf_extension(filename):
    """
    Checking if the file has the ending pdf
    :param filename: file that should be uploaded
    :return: nothing or the validation error
    """
    import os
    ext = os.path.splitext(filename.name)[1]
    if ext != ".pdf":
        raise ValidationError("Es sind nur Datein mit Endung .pdf erlaubt.")


class Category(models.Model):
    """
    name: the catgeorys name
    """

    # pylint: disable = too-few-public-methods
    class Meta:
        """
        Meta data for the model
        In this case the singular and plural name that will be seen in the admin interface
        """
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    name = models.CharField(verbose_name='Titel', max_length=1000,
                            help_text='Bezeichnung der Kategorie', default="Sonstiges")

    def __str__(self):
        """
        Name for the admin interface
        :return: the name of the category
        """
        return str(self.name)


class Material(models.Model):
    """
    name: short decription of what the file is about
    file: the material file
    category: category of the file
    """

    # pylint: disable = too-few-public-methods
    class Meta:
        """
        Meta data for the model
        In this case the singular and plural name that will be seen in the admin interface
        """
        verbose_name = 'Material'
        verbose_name_plural = 'Materialien'

    name = models.CharField(verbose_name='Titel', max_length=100,
                            help_text='Bezeichnung der Datei')
    file = models.FileField(verbose_name='Datei', upload_to='material/',
                            help_text="Datei hochladen.", validators=[validate_pdf_extension])
    category = models.ForeignKey(verbose_name='Kategorie', to=Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        """
        Name for the admin interface
        :return: the name of a Building
        """
        return str(self.name)

    def get_category(self):
        """
        :return: category name
        """
        if self.category is not None:
            ret = self.category.name
        else:
            ret = 'Sonstiges'
        return ret
