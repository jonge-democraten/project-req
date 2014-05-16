from django.shortcuts import render
from django.views.generic.edit import CreateView

from jd_projects.models import Project, ProjectIncomeExpenses
from jd_projects.forms import ProjectRequestForm, ExpenseIncomeFormSet

class ProjectRequestView(CreateView):
    model = Project
    slug_field = 'project_slug'
    form_class = ProjectRequestForm
    prefix = 'project'
    success_url = '/projects/request_success/'

    def form_valid(self, form):
        # If the project form is valid, we move on to checking the expected income and expenses
        income_formset = ExpenseIncomeFormSet(self.request.POST, prefix='income')
        expense_formset = ExpenseIncomeFormSet(self.request.POST, prefix='expenses')

        if 'extend_income_expenses' in self.request.POST:
            return self.form_invalid(form)
        elif income_formset.is_valid() and expense_formset.is_valid():
            response = super(ProjectRequestView, self).form_valid(form)

            # Save income/expenses for project
            for form in income_formset:
                if form.cleaned_data:
                    income = ProjectIncomeExpenses()
                    income.project = self.object
                    print form.cleaned_data
                    income.description = form.cleaned_data['description']
                    income.amount = form.cleaned_data['amount']
                    income.save()

            for form in expense_formset:
                if form.cleaned_data:
                    expense = ProjectIncomeExpenses()
                    expense.project = self.object
                    expense.description = form.cleaned_data['description']
                    expense.amount = -form.cleaned_data['amount']
                    expense.save()

            return response
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        if self.request.method in ['POST', 'PUT']:

            old_income_formset = ExpenseIncomeFormSet(self.request.POST, prefix='income')
            old_expense_formset = ExpenseIncomeFormSet(self.request.POST, prefix='expenses')

            income_initial = []
            for form in old_income_formset:
                if form.is_valid():
                    income_initial.append(form.cleaned_data)

            expense_intial = []
            for form in old_expense_formset:
                if form.is_valid():
                    expense_intial.append(form.cleaned_data)

            income_formset = ExpenseIncomeFormSet(initial=income_initial, prefix='income')
            expense_formset = ExpenseIncomeFormSet(initial=expense_intial, prefix='expenses')
        else:
            income_formset = ExpenseIncomeFormSet(prefix='income')
            expense_formset = ExpenseIncomeFormSet(prefix='expenses')

        context = {
            'expected_income_formset': income_formset,
            'expected_expense_formset': expense_formset
        }

        context.update(**kwargs)

        return super(ProjectRequestView, self).get_context_data(**context)
    
