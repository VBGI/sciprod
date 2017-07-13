#coding: utf-8

from django.db import models


class WorkType(models.Model):
    type = models.CharField(max_length=200, default='')
    abbr = models.CharField(max_legnth=2, default='')

    def __unicode__(self):
       return  self.type

class Author(models.Model):
    name = models.CharField(max_length=100)
    priority = models.PositiveIntegerField(default=0)
    work = models.ForeignKey('ScientificWork', blank=True, null=True)
    def __unicode__(self):
        return self.name + '(priority: %s)' % self.priority

class Journal(models.Model):
    name = models.CharField(max_length=300, default='', blank=True)
    impact_factor = models.FloatField(default=0.0, blank=True)

    def __unicode__(self):
        return self.name

class ComputationRules(models.Model):
    rule = models.CharField(default='', max_length=500)
    # WT = work type,
    # NP = the number of pages,
    # JIF = Journal Impact Factor


class ScientificWork(models.Model):
    name = models.CharField(max_length=300, default='',
                            verbose_name="название",
                            help_text="название научной работы")
    type = models.ForeignKey('WorkType', blank=True, null=True,
                             verbose_name="тип работы",
                             help_text="выберите тип научной работы")
    journal = models.ForeignKey('Journal', blank=True, null=True,
                                verbose_name="название журнала",
                                help_text="выберите или добавьте недостающий журнал")
    year = models.PositiveIntegerField(default=2017, blank=True,
                                       vaerbose_name="год издания",
                                       help_text="год опубликования работы")
    pages = models.CharField(max_length=15, blank=True, default='',
                             verbose_name="страницы",
                             help_text="страницы через дефис, т.е. в формате: xx-yy ")
    attachment = models.FileField(uploadto='sciprod/%Y/%m/%d',
                                  verbose_name="Файл",
                                  help_text="если файлов несколько, загрузите архив")
    link = models.URLField(blank=True, verbose_name="ссылка",
                           help_text="ссылка на Интернет ресурс")
    user = models.ForeignKey(get_user_model(), null=True, blank=True,
                             editable=False)

