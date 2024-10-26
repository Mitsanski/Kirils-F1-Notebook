import { html, render } from "/node_modules/lit-html/lit-html.js";

const root = document.querySelector("main");

export function showAbout() {
    const aboutTemplate = () => html` <h1>Welcome to about page</h1> `;

    render(aboutTemplate(), root);
}
