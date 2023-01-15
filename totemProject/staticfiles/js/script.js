// MODAL
const btnCloseModal = document.getElementById("close-modal");
const modalElm = document.getElementById("modal");

btnCloseModal.addEventListener("click", function () {
    modalElm.classList.remove("open");
});


// ACCORDION
var acc = document.getElementsByClassName("accordion");
var i;
    
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("acc-active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        } 
    });
} 