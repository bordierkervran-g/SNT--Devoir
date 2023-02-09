'use strict';
window.onload = () => {
    var state = true;
    let mainLink = document.querySelector("#MainLink");
    let presentLink = document.querySelector("#PresentLink");
    let mainPage = document.getElementById("me");
    let presentPage = document.getElementById("present");
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
        let mainOff = document.querySelector("#MainLink").offsetWidth;
        let presentOff = document.querySelector("#PresentLink").offsetWidth;
        mainPage.contentWindow.scrollTo({top: 0, behavior: 'smooth'});
        presentPage.contentWindow.scrollTo({top: 0, behavior: 'smooth'});
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
    };
};
