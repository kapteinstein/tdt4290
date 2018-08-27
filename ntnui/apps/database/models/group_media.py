from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from os import path

DEFAULT_COVER_PHOTO = "cover_photo/ntnui.png"
DEFAULT_LOGO = "logo/ntnui.svg"


def get_upload_location(type, instance, filename):
    ''' Get upload location (todo: find a way to serialize...)'''

    if not type:
        return None

    if not instance:
        return None

    if not filename:
        return None

    return path.join(type, instance.group.slug, filename)


def get_upload_cover(instance, filename):
    return get_upload_location("cover_photo", instance, filename)


def get_upload_logo(instance, filename):
    return get_upload_location("logo", instance, filename)


class GroupMediaModel(models.Model):
    media_id = models.AutoField(primary_key=True)

    cover_photo = models.ImageField(
        upload_to=get_upload_cover, default=DEFAULT_COVER_PHOTO)

    logo = models.ImageField(upload_to=get_upload_logo, default=DEFAULT_LOGO)

    group = models.OneToOneField(
        'GroupModel', on_delete=models.CASCADE, related_name='media')

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Media"
        verbose_name_plural = "Group Media"

    def __str__(self):
        return "Media object for {}".format(str(self.group))

    def logo_tag(self):
        return mark_safe('<img src={} style="height: 4rem;"/>'.format(self.logo.url if self.media_id else settings.MEDIA_URL + DEFAULT_LOGO))

    def cover_photo_tag(self):
        return mark_safe('<img src={} />'.format(self.cover_photo.url if self.media_id else settings.MEDIA_URL + DEFAULT_COVER_PHOTO))
