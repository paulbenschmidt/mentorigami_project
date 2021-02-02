from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # By defining as abstract base class, Django doesn’t create
    # core_timestampedmodel table when migrate is run
    class Meta:
        abstract = True
