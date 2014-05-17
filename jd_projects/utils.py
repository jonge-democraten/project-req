from django.core.mail import send_mail
from django.template import loader, RequestContext
from django.conf import settings
from django.db.models import Sum

def send_project_request_email(request, project):

    total_income = project.income_expenses.filter(amount__gt=0).aggregate(
        total_income=Sum('amount')
    )['total_income']

    total_expenses = -project.income_expenses.filter(amount__lt=0).aggregate(
        total_expenses=Sum('amount')
    )['total_expenses']

    context = RequestContext(request, {
        'project': project,
        'total_income': total_income,
        'total_expenses': total_expenses
    })

    email_txt_template = loader.get_template("jd_projects/email_request_body.txt")
    email_html_template = loader.get_template("jd_projects/email_request_body.html")

    # TODO: Use the HTML message too when upgrading to Django 1.7
    # Django 1.6 doesn't support HTML messages yet

    return send_mail(u"Aanvraag projectsubsidie '{}'".format(project.project_title),
                      email_txt_template.render(context),
                      project.requester_email, 
                      settings.PROJECT_REQUEST_RECIPIENTS)
