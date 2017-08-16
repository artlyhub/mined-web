from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class KeystData(models.Model):
    field_name = models.CharField(max_length=50,
                                  primary_key=True)
    field_data = JSONField()
    manager = models.ForeignKey('auth.User', related_name='keystdata', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.field_name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
