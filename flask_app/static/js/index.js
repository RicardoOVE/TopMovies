var formLogin = document.getElementById('formlogin');

formLogin.onsubmit = function(event) {
    event.preventDefault();
    var formulario = new FormData(formLogin);

    fetch("/login", {method: 'POST', body: formulario})
        .then(response => response.json())
        .then(data =>{
            console.log(data)

            setTimeout(() => {
                if(data.message == 'correct') {
                    window.location.href = "/movies";
                }
            }, 3000);

            var mensajeAlerta = document.getElementById('mensajeAlerta1');
            mensajeAlerta.innerText = data.message;
            mensajeAlerta.classList.add('alert');
            if (data.message == 'correct'){
                mensajeAlerta.classList.add('alert-success');
            } else {
                mensajeAlerta.classList.add('alert-danger');
            }
        });
}