"use strict";

window.onload = () => {
    const mainLink = document.querySelector("#MainLink");
    const presentLink = document.querySelector("#PresentLink");
    const mainPage = document.getElementById("me");
    const presentPage = document.getElementById("present");
    let state = true;

    mainLink.addEventListener("click", () => {
        state = true;
        updateDisplay();
    });

    presentLink.addEventListener("click", () => {
        state = false;
        updateDisplay();
    });

    updateDisplay();

    function updateDisplay() {
        mainPage.contentWindow.scrollTo({ top: 0, behavior: "smooth" });
        presentPage.contentWindow.scrollTo({ top: 0, behavior: "smooth" });

        if (state) {
            setMainPageDisplay();
        } else {
            setPresentPageDisplay();
        }
    }

    function setMainPageDisplay() {
        document.body.style.setProperty(
            "--W",
            mainLink.offsetWidth + 30 + "px"
        );
        document.body.style.setProperty("--M", 48 + 15 + "px");
        document.querySelector("#MainLink").style.color = "#000";
        document.querySelector("#PresentLink").style.color = "#fff";
        presentPage.style.marginLeft = 0;
        mainPage.style.opacity = 1;
    }

    function setPresentPageDisplay() {
        document.body.style.setProperty(
            "--W",
            presentLink.offsetWidth + 30 + "px"
        );
        document.body.style.setProperty(
            "--M",
            `calc(${mainLink.offsetWidth + 45}px + 48px)`
        );
        document.querySelector("#PresentLink").style.color = "#000";
        document.querySelector("#MainLink").style.color = "#fff";
        presentPage.style.marginLeft = "-100vw";
        mainPage.style.zIndex = -1;
        mainPage.style.opacity = 0;
    }
};
