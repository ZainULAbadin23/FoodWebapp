from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

# Create your models here.


class Resturant(models.Model):
    resturant_manager = models.OneToOneField(settings.AUTH_USER_MODEL,
                                             on_delete=models.CASCADE,
                                             primary_key=True)
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    resturant_name = models.CharField(unique=True, blank=False, max_length=80)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "City Resturant"
        verbose_name_plural = "City Resturants"

    def __str__(self):
        return str(self.resturant_name)


class ProductCategory(models.Model):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at',)

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="categories/products/",
                              null=True, default="default_img.jpg")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class AbstractProduct(models.Model):

    class Meta:
        abstract = True

    product_code = models.CharField(max_length=30, unique=True)
    product_name = models.CharField(max_length=50)
    product_added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=models.CASCADE,)
    slug = models.SlugField(null=True)
    my_cost = (
        models.PositiveIntegerField()
    )
    sale_price = models.PositiveIntegerField()
    product_category = models.ForeignKey(ProductCategory,
                                         on_delete=models.PROTECT)
    description = models.TextField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="products/",
                              null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Product(AbstractProduct):
    UNIT = (("qty", _("Qty")), (("piece", _("Pieces"))),
            (("serving", _("Serving"))), ("gram", _("Grams")),
            ("KG", _("KG"))
            )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    p_unit = models.CharField(max_length=10, choices=UNIT, default='qty')
