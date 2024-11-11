function ShowMenu() {
    let menu = document.getElementById("overlay"); 
    if (menu.style.display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}

function ShowDelete(pk=null) {
    let delet = document.getElementById("overlay2"); 
    let confirm = document.getElementById("deleteform");

    if(pk) {
        confirm.action = `/my_guides/delete/${pk}/`
    }

    if (delet.style.display === "none") {
        delet.style.display = "flex";
    } else {
        delet.style.display = "none";
    }
}

function PlaySound() {
    let sound = document.getElementById('get-out');
    sound.muted = false;
    sound.play();
}