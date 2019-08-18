from django.db import models
from django.conf import settings


def upload_image_path(instance, filename):
    return f'status/{instance.user}/{filename}'


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50]
    
    class Meta:
        verbose_name='Status post'
        verbose_name_plural = 'Status posts'

    @property
    def owner(self):
        return self.user
