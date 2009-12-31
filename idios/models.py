from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class ProfileBase(models.Model):
    
    user = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    
    group_content_type = models.ForeignKey(ContentType, null=True, blank=True)
    group_object_id = models.PositiveIntegerField(null=True, blank=True)
    group = generic.GenericForeignKey("group_content_type", "group_object_id")
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        abstract = True
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self, group=None):
        # @@@ make group-aware
        return reverse("profile_detail", kwargs={"username": self.user.username})
