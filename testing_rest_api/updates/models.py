from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json


def upload_image_path(instance, filename):
    return f'updates/{instance.user}/{filename}'


class SerializedQs(models.QuerySet):
    def serialized_qs(self):
        fields = ('user', 'content', 'updated', 'timestamp')
        return serialize('json', self, fields=fields)

    def serialize(self):
        values = list(self.values('id', 'content', 'image', 'user'))
        return json.dumps(values)


class SerializedObjsManager(models.Manager):
    def get_queryset(self):
        return SerializedQs(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    serializeobj = SerializedObjsManager()

    def __str__(self):
        return self.content or f'No content for id:{self.id}'

    def serialize(self):
        try:
            image = self.img.url
        except:
            image = 'No Image'
        data = {
            'id': self.id,
            'content': self.content,
            'image': image,
            'user': self.user.id,
        }
        return json.dumps(data)


