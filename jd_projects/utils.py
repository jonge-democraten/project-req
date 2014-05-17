from django.core.email import send_email
from django.template import RequestContext
from django.shortcuts import render
from django.conf import settings
from django.db.models import Sum

def send_project_request_email(request, project):

    total_income = project.income_expenses.filter(amount__gt=0).aggegrate(
        total_income=Sum('amount')
    )['total_income']

    total_expenses = -project.income_expenses.filter(amount__lt=0).aggegrate(
        total_expenses=Sum('amount')
    )['total_expenses']

    context = RequestContext(request, {
        'total_income': total_income,
        'total_expenses': total_expenses
    })
    email_body_txt = render(request, "jd_projects/email_request_body.txt", 
                            context_instance=context)
    email_body_html = render(request, "jd_projects/email_request_body.html",
                             context_instance=context)

    # TODO: Use the HTML message too when upgrading to Django 1.7
    # Django 1.6 doesn't support HTML messages yet

    return send_email(u"Aanvraag projectsubsidie '{}'".format(project.project_title),
                      email_body_txt,
                      project.requester_email, 
                      settings.PROJECT_REQUEST_RECIPIENTS)
