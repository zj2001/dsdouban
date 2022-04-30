# Generated by Django 3.2.5 on 2022-04-24 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_translator', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('intro', models.CharField(blank=True, max_length=800, null=True)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('price_standard', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price_vip', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('edition', models.CharField(blank=True, max_length=45, null=True)),
                ('storage', models.IntegerField(blank=True, null=True)),
                ('introduction', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('parent_class', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'book_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('logistics_id', models.AutoField(primary_key=True, serialize=False)),
                ('logistics_name', models.CharField(max_length=30, unique=True)),
                ('logistics_tele', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'logistics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('submission_time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('press_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('contact', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('tele', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'press',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=40)),
                ('is_vip', models.IntegerField(default=0)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='AdminSystem.book')),
            ],
            options={
                'db_table': 'book_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='AdminSystem.order')),
                ('number', models.IntegerField()),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.BigIntegerField(default=1, primary_key=True, serialize=False)),
                ('submission_time', models.TimeField(auto_now=True)),
                ('comment', models.CharField(max_length=800)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AdminSystem.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AdminSystem.user')),
            ],
            options={
                'unique_together': {('book', 'user', 'submission_time')},
            },
        ),
    ]
