from django.core.email import send_email
from django.template import RequestContext
from django.shortcuts import render

def send_project_request_email(request, project):
    email_body_txt = render(request, "jd_projects/email_request_body.txt", 
                            context_instance=RequestContext(request))
    email_body_html = render(request, "jd_projects/email_request_body.html",
                             context_instance=RequestContext(request))

    return send_email(u"Aanvraag projectsubsidie '{}'".format(project.project_title),
                      email_body_txt,
                      project.requester_email, 
                      ['penningmeester@jd.nl'],
                      html_message=email_body_html)

