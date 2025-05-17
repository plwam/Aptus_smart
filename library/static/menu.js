function openModal() {
    document.getElementById("menuModal").style.display="flex";
}
function closeModal() {
    document.getElementById("menuModal").style.display="none";
}
window.onclick = function(event) {
    let modal = document.getElementById("menuModal");
    if (event.traget == modal) {
        modal.style.display ="none";
    }
}