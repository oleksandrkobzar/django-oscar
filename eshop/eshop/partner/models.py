from django.db import models

from oscar.apps.partner.abstract_models import AbstractPartner

class Partner(AbstractPartner):
    img_url = models.URLField()

from oscar.apps.partner.models import *  # noqa isort:skip
