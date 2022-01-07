from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .menegers import CustomUserManagar
# Create your models here.

class UserByPhoneNumber(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("Ism"), max_length=50)
    last_name = models.CharField(_("Familya"), max_length=50)
    phone_number = models.IntegerField(_("Telefon Raqam"), unique=True, null=True )
    address = models.CharField(_("Manzil"), max_length=100)
    age = models.IntegerField(_('Yosh'), null=True)
    joined_date = models.DateTimeField(_("Ro'yhatga olingan vaqt"), auto_now_add=True)


    is_active = models.BooleanField(_("Active"), default=True)
    staff = models.BooleanField(_("Staff"), default=False)
    superuser = models.BooleanField(_("Admin"), default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = CustomUserManagar()
