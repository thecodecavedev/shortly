let form = document.getElementById("form");

form.addEventListener('submit', function(e){
    e.preventDefault()
    fetch('/shorten',{
        method:"POST",
        body: new FormData(this)
    }).then(response => response.json()
)
    .then(data=>{
        console.log(data);
        document.getElementById('shortly').innerText = data.message;
    })
}

)