// Make sure the UiKit Switcher is set to the correct tab when loading (based on hash)
window.onload = function() {};

document.onreadystatechange = function(e) {
    if (document.readyState === "complete") {
        const index = window.location.hash.split("#")[1];

        if (index > 0 && index < 3) {
            // Switch to the tab based on the hash
            UIKit.switcher("#group-member-switcher").beforeshow(index);
        }
    }
};
