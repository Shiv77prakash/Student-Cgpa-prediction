document.querySelector("form").addEventListener("submit", function(e) {
    let inputs = document.querySelectorAll("input");

    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].value === "") {
            alert("Fill all fields!");
            e.preventDefault();
            return;
        }
    }
});