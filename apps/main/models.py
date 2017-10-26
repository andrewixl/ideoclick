from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

class Client(models.Model):
    client_name = models.CharField(_("Client Name"), max_length=255)
    client_image = models.ImageField(_("Image"), upload_to='media/clients/', default='media/None/no-img.jpg')
    client_type = models.CharField(max_length=256, choices=[('normal', 'Normal'), ('large', 'Large')])

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.client_name + " - " + self.client_type
