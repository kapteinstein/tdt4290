from forms.models import *
from forms.models import CoachSigningForm, CoachFormModel

# Add here when creating a new type of form
FORM_TYPES = {
    'coach': CoachFormModel,
}

signing_forms = {
    CoachFormModel.form_slug: CoachSigningForm,

}