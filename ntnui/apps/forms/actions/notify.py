from django.core.mail import send_mail
from .action_abstract_class import Action


class Notify(Action):

  def __init__(self, subject, body, emails, url):
    self.subject = subject
    self.body = body
    self.emails = emails
    self.url = url

  def do(self):
    for email in self.emails: 
        send_mail(self.subject, self.body + self.url, "no-reply@ntnui.no", [email])


#Returns a function taking a child of AbstractFormModel as a child that when called returns a object of the Notify-class
def notify(email_data):
    def generate_notify_class(form):
        emails = email_data["get_emails_from_form"](form)
        url = define_url(form.form_slug, form.pk, email_data["url_template"])
        return Notify(email_data["subject"], email_data["body"], emails, url)
    return generate_notify_class



def define_url(slug, private_key, url_string):
    return url_string.format(slug, private_key)



# Functions that takes in child of a AbstractFormModel and returns and array of email strings
def emails_notify_signers(form):
    return form.form_signers.all().values_list('email', flat=True)

def emails_notify_approvers(form):
    return form.form_approvers.all().values_list('email', flat=True)

def emails_notify_owner(form):
    return [form.form_instantiator.email]


# Defines the data for the different notification types
notification_email_data = {
  "notify_signers": {
    "subject": "Hei, du har et nytt skjema du skal signere",
    "body": "Følgende skjema er utsendt til signering av deg ",
    "url_template": "http://localhost:8000/f/signer-info/{}/{}/",
    "get_emails_from_form": emails_notify_signers,
  },
  "notify_approvers": {
    "subject": "Hei, du har et nytt skjema du skal godkjenne",
    "body": "Følgende skjema er utsendt til godkjenning av deg ",
    "url_template": "http://localhost:8000/f/signer-info/{}/{}/",
    "get_emails_from_form": emails_notify_approvers,
  },
  "notify_owner": {
    "subject": "Hei, skjemaet er blitt signert",
    "body": "Skjemaet er fullført, du finner det blant fullførte signeringer ",
    "url_template": "http://localhost:8000/f/",
    "get_emails_from_form": emails_notify_owner,
  },
}

# Since notify is run on initialization the keys action_create will contain functionas that return a object of the Notify-class on instantiation
notification_object_creators = {
    "notify_signers": {
        "action_creator": notify(notification_email_data["notify_signers"]),
        "status_message": "Send mail til signerere",
    },
    "notify_approvers": {
        "action_creator": notify(notification_email_data["notify_approvers"]),
        "status_message": "Send mail til godkjennere",
    },
    "notify_owner":  {
        "action_creator": notify(notification_email_data["notify_owner"]),
        "status_message": "Send mail til eier av skjema om at det er fullført"
    }
}