document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", (e) => {
            if (!confirm("Confirm submission?")) {
                e.preventDefault();
            }
        });
    }
});
