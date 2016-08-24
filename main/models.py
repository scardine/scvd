# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dado(models.Model):
    localidade = models.ForeignKey('Localidade', blank=True, null=True)
    localidade_descricao = models.CharField(max_length=250, blank=True, null=True)
    indicador = models.ForeignKey('Indicador')
    indicadorid_alfa = models.CharField(max_length=50, blank=True, null=True)
    ano = models.TextField(blank=True, null=True)  # This field type is a guess.
    dado_valor = models.CharField(u"Valor", max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_dado'


class Fonte(models.Model):
    fonte_id = models.BigAutoField(primary_key=True)
    fonte_descricao = models.CharField(u"Descrição", max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.fonte_descricao

    class Meta:
        # managed = False
        db_table = 'appind_fonte'


class Grupo(models.Model):
    grupo_id = models.IntegerField(primary_key=True)
    grupo_nome = models.CharField(u"Nome", max_length=25, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_grupo'

    def __unicode__(self):
        return self.grupo_nome


class Indicador(models.Model):
    indicador_id = models.IntegerField(primary_key=True)
    indicador_formato = models.CharField(u"Formato", max_length=10)
    indicador_nome = models.CharField(u"Nome", max_length=250, blank=True, null=True)
    indicador_periodo = models.CharField(u"Período", max_length=50, blank=True, null=True)
    indicador_descricao = models.CharField(u"Descrição", max_length=250, blank=True, null=True)
    indicador_observacao = models.CharField(u"Observação", max_length=250, blank=True, null=True)
    temas = models.ManyToManyField(u'Tema', through='TemaIndicador')
    fontes = models.ManyToManyField(u'Fonte', through='IndicadorFonte')

    class Meta:
        # managed = False
        db_table = 'appind_indicador'
        verbose_name_plural = u'Indicadores'


class IndicadorFonte(models.Model):
    indicador = models.ForeignKey(Indicador)
    fonte = models.ForeignKey(Fonte)

    class Meta:
        # managed = False
        db_table = 'appind_indicador_fonte'
        verbose_name_plural = u'Indicador x Fonte'


class Localidade(models.Model):
    localidadeid7 = models.IntegerField(db_column='localidadeId7')  # Field name made lowercase.
    localidade_id = models.IntegerField(primary_key=True)
    regiao_id = models.SmallIntegerField()
    localidade_descricao = models.CharField(u"Descricao", max_length=250)
    localidade_ordem = models.SmallIntegerField(u"Ordem")
    tipoloc = models.ForeignKey('TipoLoc')
    localidade_alvo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_localidade'

    def __unicode__(self):
        return self.localidade_descricao


class Mapa(models.Model):
    localidade = models.ForeignKey(Localidade)
    localidade_descricao = models.CharField(max_length=250)
    tipoloc = models.ForeignKey('TipoLoc')
    localidadetopojson = models.CharField(db_column='localidadeTopoJson', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'appind_mapas'

    def __unicode__(self):
        return self.localidade_descricao


class Tema(models.Model):
    tema_id = models.AutoField(primary_key=True)
    tema_descricao = models.CharField(max_length=120)
    tema_ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_tema'
        ordering = ('tema_ordem', 'tema_descricao')

    def __unicode__(self):
        return self.tema_descricao


class TemaIndicador(models.Model):
    tema = models.ForeignKey(Tema)
    indicador = models.ForeignKey(Indicador)

    class Meta:
        # managed = False
        db_table = 'appind_tema_indicador'


class TipoLoc(models.Model):
    tipoloc_id = models.AutoField(primary_key=True)
    tipoloc_descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_tipo_loc'
        verbose_name_plural = u"Tipos de Localidade"
        verbose_name = u"Tipo de Localidade"

    def __unicode__(self):
        return self.tipoloc_descricao


class Uf(models.Model):
    uf_id = models.IntegerField(primary_key=True)
    uf_nome = models.CharField(u"Nome", max_length=19, blank=True, null=True)
    uf_sigla = models.CharField(u"Sigla", max_length=2, blank=True, null=True)
    uf_centroide = models.CharField(u"Centróide", max_length=50, blank=True, null=True)
    uf_zoom = models.IntegerField(blank=True, null=True)
    uf_ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_uf'
        verbose_name = u"UF"

    def __unicode__(self):
        return self.uf_nome


class Unidade(models.Model):
    unidade_id = models.AutoField(primary_key=True)
    unidade_descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appind_unidade'

    def __unicode__(self):
        return self.unidade_descricao


class FluxoTbDados(models.Model):
    fluxo_id = models.BigAutoField(primary_key=True)
    indicador = models.ForeignKey(Indicador, blank=True, null=True)
    ano = models.BigIntegerField(blank=True, null=True)
    localidade_origem = models.ForeignKey(Localidade, blank=True, null=True, related_name='origens')
    localidade_destino = models.ForeignKey(Localidade, blank=True, null=True, related_name='destinos')
    dado_valor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'fluxo_tb_dados'


class ProjpopTbDicionario(models.Model):
    dic_id = models.IntegerField(primary_key=True)
    dic_ref = models.CharField(max_length=10)
    dic_descricao = models.CharField(max_length=250)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_dicionario'


class ProjpopTbDrs(models.Model):
    drs_id = models.IntegerField(primary_key=True)
    drs_ref = models.CharField(max_length=6)
    drs_descricao = models.CharField(max_length=25)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_drs'


class FaixaEtaria(models.Model):
    faixa_id = models.AutoField(primary_key=True)
    faixa_descricao = models.CharField(max_length=15)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_faixaetaria'


class ProjpopTbMunicipio(models.Model):
    mun_id = models.IntegerField(primary_key=True)
    mun_descricao = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_municipio'


class ProjpopTbPopulacao(models.Model):
    mun_id = models.IntegerField()
    regsau_id = models.IntegerField()
    drs_id = models.IntegerField()
    drs_ref = models.CharField(max_length=6)
    rras_id = models.IntegerField()
    ano = models.IntegerField()
    faixa_id = models.IntegerField(blank=True, null=True)
    sexo_id = models.IntegerField(blank=True, null=True)
    populacao = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_populacao'


class ProjpopTbRegsaude(models.Model):
    regsau_id = models.IntegerField(primary_key=True)
    regsau_descricao = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_regsaude'


class ProjpopTbSexo(models.Model):
    sexo_id = models.AutoField(primary_key=True)
    sexo_ref = models.CharField(max_length=1)
    sexo_descricao = models.CharField(max_length=10)

    class Meta:
        # managed = False
        db_table = 'projpop_tb_sexo'


class Tbindtemp(models.Model):
    temaid = models.IntegerField(db_column='temaId')  # Field name made lowercase.
    temanome = models.CharField(db_column='temaNome', max_length=150, blank=True, null=True)  # Field name made lowercase.
    indicadorid = models.IntegerField(db_column='indicadorId')  # Field name made lowercase.
    indicadoridalfa = models.CharField(db_column='indicadorIdAlfa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indicadornome = models.CharField(db_column='indicadorNome', max_length=250, blank=True, null=True)  # Field name made lowercase.
    indicadornomenovo = models.CharField(db_column='indicadorNomeNovo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    indicadorperiodo = models.CharField(db_column='indicadorPeriodo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indicadorobs = models.CharField(db_column='indicadorObs', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'tbindtemp'
