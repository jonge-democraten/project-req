from django import forms
from django.forms.models import modelform_factory
from django.forms.formsets import formset_factory
from form_utils.forms import BetterForm, BetterModelForm
from localflavor.nl.forms import NLZipCodeField, NLPhoneNumberField
from jd_projects.models import Project, ProjectIncomeExpenses

class ProjectRequestForm(BetterModelForm):
    class Meta:
        model = Project
        widgets = {
            'requester_postcode': NLZipCodeField(),
            'requester_phone': NLPhoneNumberField()
        }

        fieldsets = [
            ('Project details', {
                'fields': ['project_title', 'project_org', 'project_location', 'project_date', 'project_desc',
                           'project_goal'],
                'description': 'Details van het project zelf.'
            }),
            ('Aanvrager', {
                'fields': ['requester_org', 'requester_name', 'requester_title', 'requester_address', 
                           'requester_postcode', 'requester_city', 'requester_email', 'requester_phone'],
                'description': 'Gegevens van de aanvrager.'
            })
        ]

class ExpenseIncomeForm(BetterForm):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=6, decimal_places=2)

ExpenseIncomeFormSet = formset_factory(ExpenseIncomeForm, extra=3)


