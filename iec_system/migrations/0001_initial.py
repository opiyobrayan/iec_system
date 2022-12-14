# Generated by Django 4.1.3 on 2022-12-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IecMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='material Title')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='author')),
                ('description', models.CharField(choices=[('book', 'book'), ('poster', 'poster'), ('flier', 'flier'), ('notebook', 'notebook'), ('booklet', 'booklet'), ('banner', 'banner')], max_length=200, verbose_name='Description')),
                ('thematic', models.CharField(blank=True, choices=[('SRHR', 'SRHR'), ('H&G', 'H&G'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU')], max_length=200, null=True, verbose_name='Thematic')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('dates', models.DateField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='your name')),
                ('copies_requested', models.IntegerField(blank=True, null=True, verbose_name='copies requested')),
                ('copies_returned', models.IntegerField(blank=True, null=True, verbose_name='copies returned')),
            ],
        ),
    ]
