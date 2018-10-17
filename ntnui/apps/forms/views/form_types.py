from forms.models import CoachInstantiationForm, CoachSigningForm, CoachFormModel

# Add here when creating a new type of form
instantiation_forms = {
    CoachFormModel.form_slug: CoachInstantiationForm,
}

signing_forms = {
    CoachFormModel.form_slug: CoachSigningForm,

}