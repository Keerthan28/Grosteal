# Generated by Django 3.2.8 on 2021-10-25 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('characterId', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('categoryName', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('userName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phno', models.PositiveBigIntegerField(unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('productName', models.CharField(max_length=200)),
                ('productPrice', models.FloatField()),
                ('productDesc', models.TextField()),
                ('productLoc', models.TextField(blank=True, null=True)),
                ('productCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderId', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('orderQuantity', models.IntegerField()),
                ('orderDate', models.DateTimeField()),
                ('orderPhone', models.PositiveBigIntegerField()),
                ('orderStatus', models.BooleanField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.users')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
            ],
        ),
    ]
