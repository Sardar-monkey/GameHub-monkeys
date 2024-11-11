function ShowMenu() {
    let menu = document.getElementById("overlay"); 
    if (menu.style.display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}

function ShowDelete() {
    let delet = document.getElementById("overlay2"); 
    if (delet.style.display === "none") {
        delet.style.display = "flex";
    } else {
        delet.style.display = "none";
    }
}

function ShowSidebar() {
    let sidebar = document.getElementById("sidebar");
    let bottom_radius = document.getElementById("create_category");
    sidebar.style.display === "none" ? sidebar.style.display = "block" : sidebar.style.display = "none";
    bottom_radius.style.borderBottomLeftRadius === "0px" ? bottom_radius.style.borderBottomLeftRadius = "15px" : bottom_radius.style.borderBottomLeftRadius = "0px";
    bottom_radius.style.borderBottomRightRadius === "0px" ? bottom_radius.style.borderBottomRightRadius = "15px" : bottom_radius.style.borderBottomRightRadius = "0px";
}
