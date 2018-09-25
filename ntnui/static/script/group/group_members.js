// Slug available from global variable (Loaded from HTML Template)

/* API CALL METHODS */

const apiCall = (path, params) => {
    // Return a promise of a api get
    return axios({
        method: "get",
        url: path,
        params: params,
        timeout: 5000 // timeout after 5 seconds
    }).then(({ data }) => {
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

const uninviteUser = (email, slug) => {
    // Await the api GET and unpack the JSON response
    return apiCall("/api/uninvite-user", {
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

const getRequests = slug => {
    return apiCall("/api/requests", {
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
                        populateInvitations();
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
            populateRequests();
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

const createHeader = elements => {
    // Create a html header consisting of the elements
    return htmlElement({
        element: "thead",
        child: htmlElement({
            element: "tr",
            children: elements
        })
    });
};

const createBody = rows => {
    // Create a html body consisting of the rows
    return htmlElement({
        element: "tbody",
        children: rows
    });
};

const createTable = (header, body) => {
    return htmlElement({
        element: "table",
        class: "uk-table uk-table-divider uk-margin-remove-top",
        children: [header, body]
    });
};

const noTableData = message => {
    return htmlElement({
        element: "p",
        class:
            "uk-align-center uk-text-center uk-text-meta uk-margin-medium-top",
        text: message
    });
};

const switchTab = containerId => {
    // Get the containerID element, clear it and add a loader icon
    const container = document.getElementById(containerId);
    // Clear the container and place a loader into it
    container.innerHTML = "";
    container.appendChild(createLoader());

    return container;
};

const createLoader = () => {
    // Create a div with a CSS spinner (loading icon)
    return htmlElement({
        element: "div",
        class: "uk-width-1-1 uk-flex uk-flex-center",
        child: htmlElement({
            element: "div",
            "uk-spinner": "ratio: 1"
        })
    });
};

/* INVITATIONS PAGE */

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

    const td_cancel = htmlElement({
        element: "td",
        id: "member-invitation-" + user["member__pk"],
        class: "uk-text-center uk-width-1-5",
        child: htmlElement({
            element: "a",
            href: "",
            class: "uk-link-reset",
            child: htmlElement({
                element: "span",
                "uk-icon": "icon: close"
            })
        })
    });

    // Add an onclick event listener for the cancel button
    td_cancel.childNodes[0].addEventListener("click", e => {
        // Prevent the page form jumping up again...
        e.preventDefault();

        uninviteUser(user["member__email"], slug).then(response => {
            // If the invitation was successfully revoked, refresh the page and show a notification
            if (response === "InvitationRevoked") {
                notification("The invitation was revoked", "check");
                populateInvitations();
            }
        });
    });

    const tr = htmlElement({
        element: "tr",
        children: [td_name, td_email, td_time, td_cancel]
    });

    return tr;
};

const invitationTable = content => {
    return createTable(
        createHeader([
            htmlElement({
                element: "th",
                text: "Name"
            }),
            htmlElement({
                element: "th",
                class: "uk-table-expand",
                text: "Mail"
            }),
            htmlElement({
                element: "th",
                class: "uk-table-expand",
                text: "Invitation Sent"
            }),
            htmlElement({
                element: "th",
                class: "uk-text-center uk-width-1-5",
                text: "Cancel"
            })
        ]),
        createBody(content)
    );
};

const populateInvitations = () => {
    const invitations = switchTab("group-members-invitation");

    getInvitations(slug)
        .then(response => {
            invitations.innerHTML = "";

            if (response.length > 0) {
                // Map users to table rows
                const content = response.map(user => invitationRow(user));

                // Create a html table with the content
                const table = invitationTable(content);

                // Append the table to the invitations object
                invitations.appendChild(table);
            } else {
                invitations.appendChild(
                    noTableData("There are no invitations pending")
                );
            }
        })
        .catch(error => {
            console.log(error);

            // If there's an error, remove the loader and print an error message
            invitations.innerHTML = "";
            invitations.appendChild(
                noTableData("An error occurred trying to fetch the invitations")
            );
        });
};

/* REQUESTS PAGE */

const requestRow = user => {
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
                "uk-icon": "icon: check"
            })
        })
    });

    const tr = htmlElement({
        element: "tr",
        children: [td_name, td_email, td_time, td_close]
    });

    return tr;
};

const requestTable = content => {
    return createTable(
        createHeader([
            htmlElement({
                element: "th",
                text: "Name"
            }),
            htmlElement({
                element: "th",
                class: "uk-table-expand",
                text: "Mail"
            }),
            htmlElement({
                element: "th",
                class: "uk-table-expand",
                text: "Invitation Sent"
            }),
            htmlElement({
                element: "th",
                class: "uk-text-center uk-width-1-5",
                text: "Accept"
            })
        ]),
        createBody(content)
    );
};

const populateRequests = () => {
    const requests = switchTab("group-members-requests");

    getRequests(slug)
        .then(response => {
            requests.innerHTML = "";

            if (response.length > 0) {
                const content = response.map(user => requestRow(user));
                const table = requestTable(content);
                requests.appendChild(table);
            } else {
                requests.appendChild(
                    noTableData("There are no requests pending")
                );
            }
        })
        .catch(() => {
            // If there's an error, remove the loader and print an error message
            requests.innerHTML = "";
            requests.appendChild(
                noTableData("An error occurred trying to fetch the requests")
            );
        });
};
