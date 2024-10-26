import { html, render } from "/node_modules/lit-html/lit-html.js";

const root = document.querySelector("main");

export function showHome() {
    const homeTemplate = () => html` <h1>Welcome to my website</h1> `;

    render(homeTemplate(), root);
}
