from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL,
                                             on_delete=models.CASCADE,
                                             primary_key=True)
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.customer)
