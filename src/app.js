import { showAbout } from "./views/aboutView.js";
import { showHome } from "./views/homeView.js";

const views = {
    "#home": showHome,
    "#about": showAbout,
};

function showPage() {
    // get the current hash from the URL
    const hash = window.location.hash || "#home";

    views[hash]();
}

// listen for hash changes
window.addEventListener("hashchange", showPage);

// Initiliaze the first view
showPage();
