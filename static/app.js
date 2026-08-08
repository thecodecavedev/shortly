let form = document.getElementById("form");
let link_card = document.getElementById("link-card");
let copy_button = document.getElementById("copy_button")
let url = ""
let url_input = document.getElementById("url")

form.addEventListener('submit', function (e) {

    if (url_input.value.trim() !== "") {
        e.preventDefault()
        fetch('/shorten', {
            method: "POST",
            body: new FormData(this)
        }).then(response => response.json()
        )
            .then(data => {
                link_card.style.display = "flex";
                url = data.message
                document.getElementById('shortly').innerText = data.message;
            })
    } else {
        copy_button.disabled = true
    }


}

)

copy_button.addEventListener("click", function (e) {
    navigator.clipboard.writeText(url);
    alert("url copied to clipboard: " + url)
}

)