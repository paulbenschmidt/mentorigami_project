from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _  # allows translations?

# from django.db import models

# from core.models import TimeStampedModel

## Example taken from pg 66 of Two Scoops
# class Account(TimeStampedModel):
#     name = models.CharField(max_length=200)


class User(AbstractUser):

    class Types(models.TextChoices):
        LEARNER = "LEARNER", "Learner"
        MENTOR = "MENTOR", "Mentor"

    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=Types.LEARNER
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class LearnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.LEARNER)


class MentorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MENTOR)


class Learner(User):
    objects = LearnerManager()

    class Meta:
        proxy = True
    
    def learn(self):
        return "learning!"

    # Overwriting save method allow you to save users to this proxy model from this class itself
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.LEARNER
        return super().save(*args, **kwargs)


class Mentor(User):
    objects = MentorManager()

    class Meta:
        proxy = True

    def teach(self):
        return "teaching!"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.MENTOR
        return super().save(*args, **kwargs)
