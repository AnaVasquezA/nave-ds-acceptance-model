# Generated by Django 4.0.1 on 2022-09-14 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0013_rename_risk_before_acc_profilevariables_risk_before_accu'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressIne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Multiplataform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profilevariables',
            name='multiplat_score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='profilevariables',
            name='multiplat_score_motive',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilevariables',
            name='trips',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profilevariables',
            name='multiplataform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.multiplataform'),
        ),
        migrations.AlterField(
            model_name='profilevariables',
            name='adress_ine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.adressine'),
        ),
    ]
