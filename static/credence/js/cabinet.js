document.addEventListener('DOMContentLoaded', () =>{
    
    const cabinet = document.querySelector(".credence")
    const cabMenu = document.querySelector(".asteration")
    
    cabinet.addEventListener("click", () =>{
        cabinet.classList.toggle("active")
        cabMenu.classList.toggle("active")
    })

    document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () =>{
        cabinet.classList.remove("active")
        cabMenu.classList.remove("active")
    }))

})