from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

class Project(models.Model):
    project_title = models.CharField(_("project titel"), max_length=200)
    project_slug = models.SlugField(max_length=255)
    project_org = models.CharField(_("organisatie"), max_length=200)
    project_location = models.CharField(_("locatie"), max_length=255)
    project_date = models.DateTimeField(_("datum (yyyy-mm-dd)"))
    project_desc = models.TextField(_("Beschrijving"), null=True)
    project_goal = models.TextField(_("Doel"), null=True, blank=True)

    requester_org = models.CharField(_("organisatie"), max_length=200)
    requester_name = models.CharField(_("naam"), max_length=200)
    requester_title = models.CharField(_("titel"), max_length=200)
    requester_address = models.CharField(_("adres"), max_length=200)
    requester_postcode = models.CharField(_("postcode"), max_length=6)
    requester_city = models.CharField(_("stad"), max_length=50)
    requester_email = models.EmailField(_("email"))
    requester_phone = models.CharField(_("telefoon"), max_length=15)

    def save(self, *args, **kwargs):
        self.project_slug = slugify("{}-{}".format(self.project_org, self.project_title))
        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.project_title

class ProjectIncomeExpenses(models.Model):
    project = models.ForeignKey('Project')
    description = models.CharField(_("beschrijving"), max_length=255)
    amount = models.DecimalField(_("bedrag"), max_digits=6, decimal_places=2)

    def __unicode__(self):
        return "{} - {:.2f}".format(self.description, self.amount)


