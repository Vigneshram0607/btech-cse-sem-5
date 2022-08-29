function changeColor(element){
    element.style.backgroundColor = "white"
}

const grandparent = document.getElementById("grandparentid")
const gp = document.querySelector("#grandparentid")

const parents = Array.from(document.getElementsByClassName("parent"))
const ps = Array.from(document.querySelectorAll(".parent"))

// grandparent.style.backgroundColor = "grey"
// changeColor(grandparent)
// parents.forEach(changeColor)

ps.forEach(changeColor)
changeColor(gp)


