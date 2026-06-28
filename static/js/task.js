function openDeleteModal(deleteUrl, taskName) {

    const modal = document.getElementById("deleteModal");

    console.log(modal);

    if (!modal) {
        alert("deleteModal not found!");
        return;
    }

    modal.style.display = "flex";

    document.getElementById("deleteBtn").href = deleteUrl;

    document.getElementById("deleteMessage").innerHTML =
        `Are you sure you want to delete "${taskName}"?`;
}