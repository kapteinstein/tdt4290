// Slug available from global variable
const invitationModal = UIkit.modal("#group-members-invitation-modal");
const invitationForm = document.getElementById("group-members-invitation-form");
const invitationError = document.getElementById(
    "group-members-invitation-form-error"
);

// Add an eventlistener to clear the invitation form before showing the modal
UIkit.util.on("#group-members-invitation-modal", "beforeshow", () => {
    invitationError.setAttribute("class", "uk-hidden");
    invitationForm.reset();
});

// Add a onclick event listener on the invitation modal
invitationForm.addEventListener("submit", event => {
    // Prevent form submission
    event.preventDefault();

    const input = event.target.elements["invitation-email"];
    const email = input.value;
    const isValid = input.checkValidity();

    if (isValid) {
        inviteUser(email, slug)
            .then(response => {
                switch (response) {
                    case "InvitationSent":
                        invitationFormSuccess("Invitation Sent!");
                        break;
                    case "UserDoesNotExist":
                        invitationFormError(
                            "That email is not registered in the system"
                        );
                        break;
                    case "UserAlreadyInGroup":
                        invitationFormError(
                            "That user is already part of this group!"
                        );
                        break;
                    default:
                        invitationFormError(
                            "Oops, something went very wrong..."
                        );
                }
            })
            .catch(() => {
                // TODO: Adopt proper error handling practices
                invitationModal.hide();
                notification("An Error Occured!", "warning");
            });
    }

    // Prevent any resubmission
    return false;
});

const invitationFormSuccess = (message, icon = "info") => {
    invitationModal.hide();
    notification(message, icon);
};

const invitationFormError = message => {
    // Remove the hidden attribute and set the text of the error field
    invitationError.removeAttribute("class");
    invitationError.firstElementChild.textContent = message;
};

const inviteUser = (email, slug) => {
    // Await the api GET and unpack the JSON response
    return axios
        .get("/api/invite-user", {
            params: {
                email: email,
                slug: slug
            }
        })
        .then(({ data }) => {
            return data.message;
        });
};
