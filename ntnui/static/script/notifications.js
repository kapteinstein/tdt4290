// Load uikit from the window
UIKit = window.UIkit;

const notImplemented = function() {
    UIKit.notification({
        message:
            "<span class='uk-margin-small-right' uk-icon='icon: code'></span>This route is not yet implemented",
        status: "default",
        pos: "top-right",
        timeout: 2000
    });
};
