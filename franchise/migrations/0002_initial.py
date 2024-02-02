# Generated by Django 5.0.1 on 2024-01-19 18:46

import django.db.models.deletion
import phonenumber_field.modelfields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('franchise', '0001_initial'),
        ('resturant', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('franchise_manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('franchise_name', models.CharField(max_length=80, unique=True)),
                ('address', models.TextField(blank=True, default=None, max_length=255)),
            ],
            options={
                'verbose_name': 'Franchise',
                'verbose_name_plural': 'Franchises',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='purchased_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resturant.product'),
        ),
        migrations.CreateModel(
            name='Deliverer',
            fields=[
                ('deliverer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('address', models.TextField(blank=True, default=None, max_length=255)),
                ('works_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliverer', to='franchise.franchise')),
            ],
            options={
                'verbose_name': 'Delivery Person',
                'verbose_name_plural': 'Delivery Persons',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('invoice_num', models.CharField(db_index=True, default=0, max_length=50)),
                ('order_status', models.CharField(choices=[('Partially Paid', 'installment'), ('Full Payment', 'full_payment'), ('Unpaid', 'unpaid')], max_length=14)),
                ('paid_amount', models.IntegerField(default=0)),
                ('total_bill', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customer.customer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Order',
                'verbose_name_plural': 'historical Orders',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.CharField(default=0, max_length=50, unique=True)),
                ('order_status', models.CharField(choices=[('Partially Paid', 'installment'), ('Full Payment', 'full_payment'), ('Unpaid', 'unpaid')], max_length=14)),
                ('paid_amount', models.IntegerField(default=0)),
                ('total_bill', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='order', to='customer.customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': '',
                'ordering': ['-updated_at'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalCart',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('purchased_quantity', models.PositiveIntegerField()),
                ('sold_at_price', models.PositiveIntegerField()),
                ('product_discount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('purchased_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='resturant.product')),
                ('invoice_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='franchise.order')),
            ],
            options={
                'verbose_name': 'historical Single item in invoice',
                'verbose_name_plural': 'historical Single item in invoices',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='cart',
            name='invoice_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='franchise.order'),
        ),
    ]