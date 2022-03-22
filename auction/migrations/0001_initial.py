# Generated by Django 4.0.3 on 2022-03-22 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spectrum', models.CharField(max_length=100)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('round_number', models.IntegerField()),
                ('no_of_block', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BidderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spectrum', models.CharField(max_length=100)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('no_of_blocks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.IntegerField()),
                ('actionStatus', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auc_status', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.round')),
            ],
        ),
    ]
