"""
AbstractFormModel      

All models inherits from this AbstractFormModel because they share the same fields.
The Abstract Model is a super class with disjunct subclasses as drawn below.
                        _______________________
                        |                     |
                        |   Abstract Model    |
                        -----------------------
                                  ||
                                  ||
                                /----\
                                | D  |
            .___________________/-|--\_______________________.
            |                     |                          |
    ________|________    _________|___________       ________|________
    | Trustee Model |    | BoardChange Model |  ...  | Trainer Model |
    -----------------    ---------------------       -----------------
           /\                    /\                         /\
            |                     |                          |
            |           ER-model (for the database)          |
      ##############################################################
            |        Forms (not part of the database)        |
            |                     |                          |
            |                     |                          |
           \/                    \/                         \/
    _________________    _____________________       _________________
    | Trustee Form  |    | BoardChange Form  |  ...  | Trainer Form  |
    -----------------    ---------------------       -----------------

Each subclass corresponds to a Model (database table) and saves information about
a spesific form e.g, BoardChange, Trustee, Trainer, etc. Each model has one or
more forms that is presented to the user.


The abstract form has the following fields defined in the database:
        form_instantiator: The User that creates the instance of a form
        form_signers: The Users that must sign the form. This can be only
                one or several users.
        form_approvers: The Users that must approve a form that is filled
                out before the form is completed
        form_signatures: A list of all users that have signed the form with
                the required signature type.
        form_completed: Status of a form. Default is false. When all users
                that are required to sign or approve the form has signed,
                this is set to 'true'.

In addition to the database fields, each instance of the model also has the
attributes:
        form_name: Name of the form (Trustee form, BoardChange form, etc.)
        required_sign_type: Type of signature required.
                0 -> low. (password level of authentication)
                1 -> high. (paper signature or BankID)
        access_level: required user access level to be able to instantiate a
            form. See below.


--- Note about access levels ---
Every user should not be able to see and instansiate every form. A natural way
to distinguish the access rights is to implement an 'access level'-system where
each form has an associated required access_level. This system is a hierarchy
where all users with the required access level (or higher) will be able to
instansiate that particular form. The users who are able to see an instansiated
form are the form_instantiator, form_signers and form_approvers.

    access levels:
        8: admin
        7: HS
        6: Group Leader
        5: Cashier
        4: Board
        3: Trainer/Coach
        2: Group Member
        1: Member
        0: Non-member

"""

from django.db import models


class AbstractFormModel(models.Model):
    # databse fields
    form_instantiatior = models.ForeignKey('database.UserModel', on_delete=models.SET_NULL, null=True, related_name="form_instantiatior")
    form_signers = models.ManyToManyField('database.UserModel', related_name="form_signers")
    form_approvers = models.ManyToManyField('database.UserModel', related_name="form_approvers", blank=True)
    form_signatures = models.ManyToManyField('database.UserModel', related_name="form_signatures", blank=True)
    form_completed = models.BooleanField(default=False)

    # class attributes
    form_name = 'NO NAME'
    required_sign_type = 0

    def is_form_completed(self):
        return len(self.form_signatures.all()) == len(self.form_signers.all())
    # attribute spesific methods
    def get_required_sign_level(self):
        return self.required_sign_type

    def get_form_name(self):
        return self.form_name



