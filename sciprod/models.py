from django.db import models


class WorkType(models.Model):
    type = models.CharField(max_length=200, default='')

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
    name = models.CharField(max_length=300, default='')
    type = models.ForeignKey('WorkType', blank=True, null=True)
    journal = models.ForeignKey('Journal', blank=True, null=True)
    year = models.PositiveIntegerField(default=2017, blank=True)
    pages = models.CharField(max_length=15, blank=True, default='')
    attachment = models.FileField(uploadto='sciprod/%Y/%m/%d')
    link = models.URLField(blank=True)


