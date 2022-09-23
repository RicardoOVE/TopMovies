var formRegister = document.getElementById('sign_in_form');

formRegister.onsubmit = function(event) {
    event.preventDefault()
    var formularioreg = new FormData(formRegister);
    fetch("/sign_in", {method: 'POST', body: formularioreg})
        .then(response => response.json())
        .then(data =>{
            console.log(data)
            setTimeout(() => {
                if(data.message == 'correct') {
                    window.location.href = '/movies';
                }
            }, 3000);

            var mensajeAlerta2 = document.getElementById('alertmessage');
            mensajeAlerta2.innerText = data.message;
            mensajeAlerta2.classList.add('alert');
            if (data.message == 'correct'){
                mensajeAlerta2.classList.add('alert-success');
            } else {
                mensajeAlerta2.classList.add('alert-danger');
            }
            
        });
}