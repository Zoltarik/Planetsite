# Generated by Django 2.0.5 on 2018-05-10 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sotrudnuk', models.IntegerField()),
                ('custumers', models.IntegerField()),
                ('bookShipped', models.BooleanField()),
                ('openOrClosed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tblBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameBook', models.TextField()),
                ('fioAuthor', models.CharField(max_length=100)),
                ('countPage', models.IntegerField()),
                ('bookPrice', models.IntegerField()),
                ('linkImage', models.ImageField(blank=True, upload_to='img/', verbose_name='Обложка')),
                ('countBookWarhouse', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tblCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tblCustumers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fioCustumers', models.CharField(max_length=100)),
                ('addressCustumers', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tblIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberIndex', models.CharField(max_length=20)),
                ('citiName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tblPublesher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePublesher', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tblcustumers',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.tblIndex'),
        ),
        migrations.AddField(
            model_name='tblbook',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.tblCategory'),
        ),
        migrations.AddField(
            model_name='tblbook',
            name='publesher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.tblPublesher'),
        ),
    ]
