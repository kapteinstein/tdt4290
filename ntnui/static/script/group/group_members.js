document
    .getElementById("group-member-invitation-form-submit")
    .addEventListener("click", function(event) {
        event.preventDefault();
        console.log(event);
    });

axios
    .get("/api/members/" + "parks-and-recreation-department")
    .then(response => {
        console.log(response);
    })
    .catch(e => {
        console.log(e);
    });
