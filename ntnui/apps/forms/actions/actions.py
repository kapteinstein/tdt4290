from .notify import Notify, notification_object_creators

"""
    action_object_creators is a dict with elements on the form:

    {
        "action_creator": func,
        "status_message": string
    }
"""

action_object_creators = {**notification_object_creators}

class Actions():

    def __init__(self, form, type = False):
        self.form = form
        self.assign_action()

    def assign_action(self):
        self.action = action_object_creators[self.form.actions[self.form.current_action]]["action_creator"](self.form);

    def status(self):
        return action_object_creators[self.form.actions[self.form.current_action]]["status_message"]

    def do(self):
        self.action.do()
        self.form.current_action += 1
        if(len(self.form.actions) > self.form.current_action):
            self.assign_action()

        self.form.save()
