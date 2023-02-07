'use strict';
state = true;
window.onload = () => {
    state = true;
    mainLink = document.querySelector("#MainLink");
    presentLink = document.querySelector("#PresentLink");
    mainPage = document.getElementById("me");
    presentPage = document.getElementById("present");
    mainLink.addEventListener("click", () => {
        state = true;
        actualise();
    });
    presentLink.addEventListener("click", () => {
        state = false;
        actualise();
    });
    actualise();
    function actualise() {
        mainOff = document.querySelector("#MainLink").offsetWidth;
        presentOff = document.querySelector("#PresentLink").offsetWidth;
        if (state) {
            document.body.style.setProperty("--W", mainOff + 30 + "px");
            document.body.style.setProperty("--M", 48 + 15 + "px");
            document.querySelector("#MainLink").style.color = "#000";
            document.querySelector("#PresentLink").style.color = "#fff";
            presentPage.style.marginLeft = 0;
            mainPage.style.opacity = 1;
        } else {
            document.body.style.setProperty("--W", presentOff + 30 + "px");
            document.body.style.setProperty(
                "--M",
                "calc(" + (mainOff + 45) + "px + 48px)"
            );
            document.querySelector("#PresentLink").style.color = "#000";
            document.querySelector("#MainLink").style.color = "#fff";
            presentPage.style.marginLeft = "-100vw"
            mainPage.style.opacity = 0;
        }
    }
};
