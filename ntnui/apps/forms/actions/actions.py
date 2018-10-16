from .notify import Notify

def notify(subject, body, emails_func):
    def notifyClass(form):
        emails = emails_func(form)
        return Notify(subject, body, emails)
    return notifyClass

def emails_notify_signers(form):
    return form.form_signers.all().values_list('email', flat=True)

def emails_notify_approvers(form):
    return form.form_approvers.all().values_list('email', flat=True)

def emails_notify_owner(form):
    return [form.form_instantiatior.email]

action_classes = {
    "notify_signers": {
        "action_creator": notify("Hei, du har et nytt skjema du skal signere", "Følgende skjema er utsendt til signering av deg", emails_notify_signers),
        "status_message": "Send mail til signerere",
    },
    "notify_approvers": {
        "action_creator": notify("Hei, du har et nytt skjema du skal godkjenne", "Følgende skjema er utsendt til godkjenning av deg", emails_notify_approvers),
        "status_message": "Send mail til godkjennere",
    },
    "notify_owners":  {
        "action_creator": notify("Hei, skjemaet er fullført", "Skjemaet er fullført, du finner det blant fullførte signeringer", emails_notify_owner),
        "status_message": "Send mail til eier av skjema om at det er fullført"
    }
}

class Actions():

    def __init__(self, form, type = False):
        self.form = form
        self.assign_action()

    def assign_action(self):
        self.action = action_classes[self.form.actions[self.form.current_action]].action(self.form);

    def status(self):
        pass

    def do(self):
        self.action.do()
        self.form.current_action += 1
        self.assign_action()
        self.form.save()
