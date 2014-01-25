from django.shortcuts import render
from djamgo.core.urlresolvers import reverse
from django.views.generic.edit import ModelFormMixin, ProcessFormView

from jd_projects.models import Project, ProjectIncomeExpenses
from jd_projects.forms import ProjectRequestForm, ExpenseIncomeFormSet

class ProjectRequestView(ModelFormMixin, ProcessFormView):
    model = Project
    slug_field = 'project_slug'
    form_class = ProjectRequestForm
    prefix = 'project'
    success_url = reverse('request_success')

    def form_valid(self, form):
        # If the project form is valid, we move on to checking the expected income and expenses
        income_formset = ExpenseIncomeFormSet(self.request.POST, prefix='income')
        expense_formset = ExpenseIncomeFormSet(self.request.POST, prefix='expenses')

        if income_formset.is_valid() and expense_formset.is_valid():
            super(ProjectRequestView, self).form_valid(form)

            # Save income/expenses for project
            for form in income_formset:
                income = ProjectIncomeExpenses()
                income.project = self.object
                income.description = form.cleaned_data['description']
                income.amount = form.cleaned_data['amount']
                income.save()

            for form in expense_formset:
                expense = ProjectIncomeExpenses()
                expense.project = self.object
                expense.description = form.cleaned_data['description']
                expense.amount = -form.cleaned_data['amount']
                expense.save()
        else:
            self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = {
            'expected_income_formset': ExpenseIncomeFormSet(self.request.POST, prefix='income'),
            'expected_expense_formset': ExpenseIncomeFormSet(self.request.POST, prefix='expenses')
        }

        context.update(**kwargs)

        return super(ProjectRequestView, self).get_context_data(**context)
    
