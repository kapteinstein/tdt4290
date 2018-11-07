from forms.models import *
from forms.models import CoachSigningForm, CoachFormModel, TeamContractSigningForm, TeamContractFormModel

# Add here when creating a new type of form
"""
FORM_TYPES holds all the form_slugs of the respective form models.
Form slugs of new types of forms should be added here.
FORM_TYPES is used in InstantiateForm to fetch all the forms available for sending out.
"""
FORM_TYPES = {
    'coach': CoachFormModel,
    'teamcontract': TeamContractFormModel
}

"""
signing_forms holds all the django forms that are used for filling out their respective model forms.
When adding a new type of form, it's signing form should be added here.
"""
signing_forms = {
    CoachFormModel.form_slug: CoachSigningForm,
    TeamContractFormModel.form_slug: TeamContractSigningForm,

}