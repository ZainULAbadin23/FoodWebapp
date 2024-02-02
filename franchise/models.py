import uuid
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from resturant.models import Product, Resturant

from customer.models import Customer

from simple_history.models import HistoricalRecords

# Create your models here.


class Franchise(models.Model):
    franchise_manager = models.OneToOneField(settings.AUTH_USER_MODEL,
                                             on_delete=models.CASCADE,
                                             primary_key=True)
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    franchise_name = models.CharField(unique=True, blank=False, max_length=80)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Franchise"
        verbose_name_plural = "Franchises"

    def __str__(self):
        return str(self.franchise_name)


class Deliverer(models.Model):
    deliverer = models.OneToOneField(settings.AUTH_USER_MODEL,
                                     on_delete=models.CASCADE,
                                     primary_key=True)
    works_at = models.ForeignKey(Franchise,
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name="deliverer")
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Delivery Person"
        verbose_name_plural = "Delivery Persons"

    def __str__(self):
        return str(self.deliverer)


class Order(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    customer_id = models.ForeignKey(Customer,
                                    on_delete=models.CASCADE,
                                    related_name='customer_user'
                                    )
    resturant_id = models.ForeignKey(Resturant,
                                     on_delete=models.CASCADE,
                                     related_name='resturant_user'
                                     )
    deliverer_id = models.ForeignKey(Deliverer,
                                     on_delete=models.CASCADE,
                                     related_name='deliverer_user'
                                     )
    items = models.JSONField()
    grand_total = models.PositiveIntegerField(default=0)
    initiated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.initiated_at.date + "    -->     "
                   + self.customer_id + "    -->    " + self.grand_total
                   )


class Cart(models.Model):
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='user'
                                    )
    item = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             related_name='menu'
                             )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.customer_id} - {self.item}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


# Order_Status = (("Partially Paid", "installment"),
#                 ("Full Payment", "full_payment"),
#                 ("Unpaid", "unpaid"))


# class Order(models.Model):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False
#                           )
#     customer = models.ForeignKey(Customer, related_name='order',
#                                  on_delete=models.PROTECT, default=None)
#     order_status = models.CharField(max_length=14, choices=Order_Status)
#     paid_amount = models.IntegerField(default=0)
#     total_bill = models.IntegerField(default=0)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     history = HistoricalRecords()

#     def __str__(self):
#         return str(self.invoice_num) + str(" - ") + str(self.customer)

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'
#         ordering = ['-updated_at']

# class Cart(models.Model):
#     invoice_item = models.ForeignKey(Order, on_delete=models.PROTECT)
#     purchased_product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     purchased_quantity = models.PositiveIntegerField()
#     sold_at_price = models.PositiveIntegerField()
#     product_discount = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     history = HistoricalRecords()

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Single item in invoice'
#         verbose_name_plural = 'Single item in invoices'

#         ordering = ['-updated_at']

#     def __str__(self):
#         return (
#             f"{self.invoice_item.invoice_num} - {self.purchased_product}"
#         )