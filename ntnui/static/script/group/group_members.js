// Slug available from global variable (Loaded from HTML Template)

/* API CALL METHODS */

const apiCall = (path, params) => {
    // Return a promise of a api get
    return axios.get(path, { params }).then(({ data }) => {
        // Unpack the data object and return its body
        return data.message;
    });
};

const inviteUser = (email, slug) => {
    // Await the api GET and unpack the JSON response
    return apiCall("/api/invite-user", {
        email: email,
        slug: slug
    });
};

const getMembers = slug => {
    return apiCall("/api/members", {
        slug: slug
    });
};

const getUser = user_id => {
    return apiCall("/api/user", {
        user_id: user_id
    });
};

const getInvitations = slug => {
    return apiCall("/api/invitations", {
        slug: slug
    });
};

/* MODAL FORM */

// Get HTML elements
const invitationModal = UIkit.modal("#group-members-invitation-modal");
const invitationForm = document.getElementById("group-members-invitation-form");
const invitationError = document.getElementById(
    "group-members-invitation-form-error"
);

// Add an eventlistener to clear the invitation form before showing the modal
UIkit.util.on("#" + invitationModal.id, "beforeshow", () => {
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

/* DYNAMICALLY LOAD TABLES */
// Get the switcher elements
const memberSwitcher = UIkit.switcher("group-member-switcher");
const memberSwitcherContainer = document.getElementById(
    "group-member-switcher-container"
);

// Add an eventlistener to switcher container
UIkit.util.on("#" + memberSwitcherContainer.id, "shown", container => {
    // Determine the target element
    switch (container.target.id) {
        case "group-member-list":
            console.log("Switched to List");
            break;
        case "group-member-invitations":
            console.log("Switched to Invitations");
            populateInvitations();
            break;
        case "group-member-requests":
            console.log("Switched to Requests");
            break;
        default:
            console.log("Not found");
    }
});

const htmlElement = dict => {
    /* Create a new html element based on the dictionary 
    *
    *  Example of the dict object:
    *  dict = {
    *       element: 'div'          - REQUIRED
    *       child: HTMLElement      - OPTIONAL (appends the child to the element)
    *       class: 'className'      - OPTIONAL (add the className to the element)
    *  }
    *  
    */
    if (!("element" in dict)) {
        return null;
    }

    // Create the element based on the element key
    const element = document.createElement(dict["element"]);

    for (attr in dict) {
        switch (attr) {
            case "text":
                const textNode = document.createTextNode(dict[attr]);
                element.appendChild(textNode);
                break;
            case "children":
                for (let child in dict[attr]) {
                    element.appendChild(dict[attr][child]);
                }
                break;
            case "child":
                element.appendChild(dict[attr]);
                break;
            case "onclick":
                element.onclick = dict[attr];
                break;
            default:
                // By default set the value of the attribute to be an attribue of the element
                element.setAttribute(attr, dict[attr]);
        }
    }

    return element;
};

const htmlTableLoader = columns => {
    const spinner = htmlElement({ element: "div", "uk-spinner": "ratio: 1" });
    const div = htmlElement({
        element: "div",
        class: "uk-width-1-1 uk-flex uk-flex-center",
        child: spinner
    });
    const td = htmlElement({
        element: "td",
        colspan: columns,
        child: div
    });
    const tr = htmlElement({
        element: "tr",
        child: td
    });
    return tr;
};

const invitationRow = user => {
    const td_name = htmlElement({
        element: "td",
        text: user["member__first_name"] + " " + user["member__last_name"]
    });

    const td_email = htmlElement({
        element: "td",
        text: user["member__email"],
        class: "uk-text-truncate"
    });

    const td_time = htmlElement({
        element: "td",
        text: user["time"],
        class: "uk-table-expand"
    });

    const td_close = htmlElement({
        element: "td",
        id: "member-invitation-" + user["member__pk"],
        class: "uk-text-center uk-width-1-5",
        child: htmlElement({
            element: "a",
            href: "#",
            onclick: notImplemented,
            class: "uk-link-reset",
            child: htmlElement({
                element: "span",
                "uk-icon": "icon: close"
            })
        })
    });

    const tr = htmlElement({
        element: "tr",
        children: [td_name, td_email, td_time, td_close]
    });

    return tr;
};

const populateInvitations = () => {
    const invitationsTable = document.getElementById(
        "group-members-invitation-table"
    );

    // Remove any content from the table
    invitationsTable.innerHTML = "";

    // Place a loader into the table while fetching the list
    const loader = htmlTableLoader(4);

    invitationsTable.appendChild(loader);

    getInvitations(slug).then(response => {
        invitationsTable.removeChild(loader);

        for (let user in response) {
            invitationsTable.appendChild(invitationRow(response[user]));
        }
    });
};
