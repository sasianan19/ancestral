const btnCloseModal = document.getElementById("close-modal");
const modalElm = document.getElementById("modal");

btnCloseModal.addEventListener("click", function () {
    modalElm.classList.remove("open");
});


