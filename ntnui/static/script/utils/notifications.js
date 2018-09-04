const notification = (message, icon = "user", status = "default") => {
    UIkit.notification({
        message:
            "<span class='uk-margin-small-right' uk-icon='icon: " +
            icon +
            "'></span>" +
            message,
        status: status,
        pos: "top-right",
        timeout: 3000
    });
};

const notImplemented = () => {
    notification("This route is not yet implemented", "cog");
};

const notificationMessage = (message, tag) => {
    if (tag == "error") {
        notification(message, "warning", "danger");
    } else if (tag == "success") {
        notification(message, "info");
    } else {
        notification(message, "question", "warning");
    }
};
