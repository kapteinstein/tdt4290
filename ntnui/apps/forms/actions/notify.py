from django.core.mail import send_mail
from .action import Action


class Notify(Action):

  def __init__(self, subject, body, emails):
    self.subject = subject
    self.body = body
    self.emails = emails

  def do(self):
    for email in self.emails: 
        send_mail(self.subject, self.body, "no-reply@ntnui.no", [email])
