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

// Reset the search form on window reload
window.onload = () => {
    document.forms["group-search-form"].reset();
};

// Group search functionality
const groupList = document.querySelectorAll("#group-list > div");

document.getElementById("group-search").onkeyup = e => {
    e = e || window.event;

    const input = this.value
        .trim()
        .replace(/ +/g, "") // Replace all spaces
        .toLowerCase();

    groupList.forEach(function(group) {
        const group_id = group.attributes.id.value.replace(/-+/g, "");
        if (group_id.includes(input)) {
            group.style.display = "block";
        } else {
            group.style.display = "none";
        }
    });
};

const showGroupModal = group => {
    // TODO: Retrieve group information from api
    UIkit.modal.dialog(`
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <div class="uk-modal-header">
            <h2 class="uk-modal-title">${group.name}</h2>
        </div>
        <div class="uk-modal-body">
            <p>${group.meta__description}</p>
        </div>
        <div class="uk-modal-footer uk-text-right">
            <button class="uk-button uk-button-default uk-modal-close" type="button">Cancel</button>
            <button class="uk-button uk-button-primary" type="button">${
                group.access === "O" ? "Join" : "Request"
            }</button>
        </div>
`);
};

const getGroupInfo = slug => {
    return apiCall("/api/group-info", {
        slug: slug
    });
};

const createGroupModal = slug => {
    getGroupInfo(slug)
        .then(groupInfo => {
            showGroupModal(groupInfo);
        })
        .catch(e => {
            console.log(e);
        });
};

const groupModals = Array.from(
    document.getElementsByClassName("ntnui-group-modal")
);

groupModals.forEach(group => {
    group.addEventListener("click", () => createGroupModal(group.id));
});
