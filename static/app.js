let form = document.getElementById("form");
let copy_button = document.getElementById("copy_button");
let url = ""

form.addEventListener('submit', function(e){
    e.preventDefault()
    fetch('/shorten',{
        method:"POST",
        body: new FormData(this)
    }).then(response => response.json()
)
    .then(data=>{
        copy_button.style.display = "block";
        url = data.message
        document.getElementById('shortly').innerText = data.message;
    })
}

)

copy_button.addEventListener("click", function(e){
    navigator.clipboard.writeText(url);
    alert("url copied to clipboard: "+url)
}

)