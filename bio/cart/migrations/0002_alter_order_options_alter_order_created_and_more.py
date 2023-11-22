# Generated by Django 4.0.4 on 2022-05-05 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, through='cart.ProductsInOrder', to='catalog.product', verbose_name='Products'),
        ),
        migrations.AlterField(
            model_name='productsinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='productsinorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='count_in_order', to='catalog.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='productsinorder',
            name='quantity',
            field=models.PositiveSmallIntegerField(verbose_name='Quantity of goods in the order'),
        ),
    ]