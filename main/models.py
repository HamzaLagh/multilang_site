from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(_('Titre'), max_length=200)
    content = models.TextField(_('Contenu'))
    publication_date = models.DateTimeField(_('Date de publication'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
