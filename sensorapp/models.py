# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipamento(models.Model):
    id_equip = models.IntegerField(primary_key=True)
    no_equipamento = models.CharField(unique=True, max_length=30)
    no_descricao = models.CharField(max_length=60)
    st_equip = models.IntegerField()
    id_local = models.ForeignKey('Local', models.DO_NOTHING, db_column='id_local', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento'


class Equipamentosensor(models.Model):
    id_equip = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='id_equip', blank=True, null=True)
    id_sensor = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='id_sensor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamentosensor'
        unique_together = (('id_equip', 'id_sensor'),)


class Leitura(models.Model):
    no_equip = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='no_equip')
    no_sensor = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='no_sensor')
    vl_leitura = models.FloatField()
    dt_leitura = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leitura'


class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    no_local = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    no_sensor = models.CharField(unique=True, max_length=15)
    no_descricao = models.CharField(max_length=60)
    id_unidade = models.ForeignKey('Unidade', models.DO_NOTHING, db_column='id_unidade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'


class Unidade(models.Model):
    id_unidade = models.AutoField(primary_key=True)
    no_unidade = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'unidade'
