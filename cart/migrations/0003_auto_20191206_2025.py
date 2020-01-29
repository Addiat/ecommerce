# Generated by Django 2.2.6 on 2019-12-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('available_in_stock', models.IntegerField(default=1)),
                ('review', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]
