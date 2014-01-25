from django.db import models

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_org = models.CharField(max_length=200)
    project_location = models.CharField(max_length=255)
    project_date = models.DateTimeField()
    project_desc = models.TextField(null=True)
    project_goal = models.TextField(null=True, blank=True)

    requester_org = models.CharField(max_length=200)
    requester_name = models.CharField(max_length=200)
    requester_title = models.CharField(max_length=200)
    requester_address = models.CharField(max_length=200)
    requester_postcode = models.CharField(max_length=6)
    requester_city = models.CharField(max_length=50)
    requester_email = models.EmailField()
    requester_phone = models.CharField(max_length=15)

    def __unicode__(self):
        return self.project_title

class ProjectIncomeExpenses(models.Model):
    project = models.ForeignKey('Project')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=2)

    def __unicode__(self):
        return "{} - {:.2f}".format(self.description, self.amount)


