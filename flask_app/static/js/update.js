var formUpdate = document.getElementById('update_form');

formUpdate.onsubmit = function(event) {
    event.preventDefault()
    var formulariupdate = new FormData(formUpdate);
    fetch("/update/user", {method: 'POST', body: formulariupdate})
        .then(response => response.json())
        .then(data =>{
            console.log(data)
            setTimeout(() => {
                if(data.message == 'correct') {
                    window.location.href = '/';
                }
            }, 3000);

            var alertmessage = document.getElementById('alertmessage');
            alertmessage.innerText = data.message;
            alertmessage.classList.add('alert');
            if (data.message == 'correct'){
                alertmessage.classList.add('alert-success');
            } else {
                alertmessage.classList.add('alert-danger');
            }
            
        });
}