# Generated by Django 5.1.7 on 2025-04-03 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarListing', '0004_carpurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='CarListing.carmodel')),
            ],
        ),
    ]
