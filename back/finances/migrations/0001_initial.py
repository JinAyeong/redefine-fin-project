# Generated by Django 4.2.6 on 2024-05-23 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField(null=True)),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField(null=True)),
                ('fin_co_no', models.TextField(null=True)),
                ('kor_co_nm', models.TextField(null=True)),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField(null=True)),
                ('join_way', models.TextField(null=True)),
                ('mtrt_int', models.TextField(null=True)),
                ('spcl_cnd', models.TextField(null=True)),
                ('join_deny', models.IntegerField(null=True)),
                ('join_member', models.TextField(null=True)),
                ('etc_note', models.TextField(null=True)),
                ('max_limit', models.TextField(null=True)),
                ('dcls_strt_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(null=True)),
                ('intr_rate_type', models.TextField(null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=100, null=True)),
                ('rsrv_type', models.TextField(null=True)),
                ('rsrv_type_nm', models.TextField(null=True)),
                ('save_trm', models.IntegerField(null=True)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.savingproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=100, null=True)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.IntegerField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finances.depositproducts')),
            ],
        ),
    ]
