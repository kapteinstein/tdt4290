// Load uikit from the window
UIKit = window.UIkit;

const notification = function(message, icon = "user", status = "default") {
    UIKit.notification({
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

const notImplemented = function() {
    notification("This route is not yet implemented", "cog");
};

const notificationMessage = function(message, tag) {
    console.log(tag);

    if (tag == "error") {
        notification(message, "warning", "danger");
    } else if (tag == "success") {
        notification(message, "info");
    } else {
        notification(message, "question", "warning");
    }
};
