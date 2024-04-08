console.log('teste')
const url = window.location.href
const caixa = document.getElementById('caixa')


$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        data = response.data // Atribuindo a response.data à variável data
        data.forEach(el=> {
            for (const [questao, resposta] of Object.entries(el)) {
                caixa.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${questao}</b>
                    </div>
                `
                resposta.forEach(resposta=> {
                    caixa.innerHTML += `
                        <div>
                            <input type="radio" class="resp" id="${questao}-${resposta}" name="${questao}" value="${resposta}">
                            <label for="${questao}">${resposta}</label>
                        </div>
                    `
                })
            }
        })
    },
    error: function(error){
        console.log(error)
    }
})

const formulario = document.getElementById('formulario')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const enviarDados = () => {
    let data = {};
    const elementos = [...document.getElementsByClassName('resp')]
    data['csrfmiddlewaretoken'] = csrf[0].value

    // Cabeçalho CSRFToken
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", csrf[0].value);
            }
        }
    });

    elementos.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        }
        else {
            if (!data[el.name]) {
            data[el.name] = null
            }
        }
    })


    $.ajax({
        type: 'POST',
        url: `${url}salvar/`,
        data: data,
        success: function(response) {
            console.log(response)
        },
        error: function(error) {
            console.log(error)
        }

    })
}

// Adicionando um ouvinte de evento para o formulário
formulario.addEventListener('submit', e=> {
    e.preventDefault(); // Prevenir o comportamento padrão do formulário
    enviarDados(); // Chamar a função para enviar os dados
});