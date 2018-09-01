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
