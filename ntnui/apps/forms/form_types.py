from forms.models import *
from forms.models import CoachSigningForm, CoachFormModel, TeamContractSigningForm, TeamContractFormModel

# Add here when creating a new type of form
FORM_TYPES = {
    'coach': CoachFormModel,
    'teamcontract': TeamContractFormModel
}

signing_forms = {
    CoachFormModel.form_slug: CoachSigningForm,
    TeamContractFormModel.form_slug: TeamContractSigningForm,

}